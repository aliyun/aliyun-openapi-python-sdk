# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

import os
import json
import time
import logging

from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstanceAttributeRequest
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
from aliyunsdkecs.request.v20140526 import StartInstanceRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from aliyunsdkecs.request.v20140526 import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


class TestEcsIntegration(object):
    def test_ecs(self):

        # init client
        client = AcsClient(
            os.environ['ACCESS_KEY_ID'],
            os.environ['ACCESS_KEY_SECRET'],
            "cn-hangzhou"
        )
        mylogger.info("Init client success")

        # get demo instance attributes
        image_id, security_group_id = TestEcsIntegration.get_demo_ecs_attributes(client)

        # create
        instance_id = TestEcsIntegration.create_instance(client, image_id, security_group_id)

        # wait
        TestEcsIntegration.wait_for_instance(client, instance_id, 'Stopped')

        # start
        TestEcsIntegration.start_instance(client, instance_id)

        # wait
        TestEcsIntegration.wait_for_instance(client, instance_id, 'Running')

        # stop
        TestEcsIntegration.stop_instance(client, instance_id)

        # wait
        TestEcsIntegration.wait_for_instance(client, instance_id, 'Stopped')

        # delete
        TestEcsIntegration.delete_instance(client, instance_id)

        # wait
        TestEcsIntegration.wait_for_instance(client, instance_id, 'Deleted')

        # delete all test instances
        TestEcsIntegration.delete_all_test_ecs_instance(client)

    @staticmethod
    def get_demo_ecs_attributes(client):
        mylogger.info("trying to get demo instance attributes...", )
        demo_instance_id = os.environ['DEMO_ECS_INSTANCE_ID']
        request = DescribeInstanceAttributeRequest.DescribeInstanceAttributeRequest()
        request.set_accept_format("JSON")
        request.set_InstanceId(demo_instance_id)
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success")
        return response.get('ImageId'), response.get('SecurityGroupIds').get('SecurityGroupId')[0]

    @staticmethod
    def create_instance(client, image_id, security_group_id):
        mylogger.info("trying to create instance...", )
        request = CreateInstanceRequest.CreateInstanceRequest()
        request.set_accept_format("JSON")
        request.set_ImageId(image_id)
        request.set_InstanceName('SdkIntegrationTestInstance' + str(int(time.time())))
        request.set_SecurityGroupId(security_group_id)
        request.set_InstanceType('ecs.t1.small')
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success")
        return response.get('InstanceId')

    @staticmethod
    def start_instance(client, instance_id):
        mylogger.info("trying to start instance...", )
        request = StartInstanceRequest.StartInstanceRequest()
        request.set_accept_format("JSON")
        request.set_InstanceId(instance_id)
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success")
        return response.get('InstanceId')

    @staticmethod
    def stop_instance(client, instance_id):
        mylogger.info("trying to stop instance...", )
        request = StopInstanceRequest.StopInstanceRequest()
        request.set_accept_format("JSON")
        request.set_InstanceId(instance_id)
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success")
        return response.get('InstanceId')

    @staticmethod
    def delete_instance(client, instance_id):
        mylogger.info("trying to delete instance...", )
        request = DeleteInstanceRequest.DeleteInstanceRequest()
        request.set_accept_format("JSON")
        request.set_InstanceId(instance_id)
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success")
        return response.get('InstanceId')

    @staticmethod
    def wait_for_instance(client, instance_id, target_status):
        while True:
            request = DescribeInstanceAttributeRequest.DescribeInstanceAttributeRequest()
            request.set_InstanceId(instance_id)
            request.set_accept_format("JSON")
            code, headers, body = client.get_response(request)
            if target_status == 'Deleted' and code == 404:
                mylogger.info("delete ecs instance(%s) success" % instance_id)
                break
            if code != 200:
                mylogger.error("Failed to describe ecs instance, statusCode=%s, message=%s" % (status, body))
                break

            status = json.loads(body.decode('utf-8')).get('Status')
            if status == target_status:
                mylogger.info(
                    "ecs instance(%s) status has changed to %s, wait 20 seconds" % (instance_id, target_status))
                time.sleep(20)
                break
            else:
                mylogger.info(
                    "ecs instance(%s) status is %s, wait for changing to %s" % (instance_id, status, target_status))
                time.sleep(10)

    @staticmethod
    def delete_all_test_ecs_instance(client):
        mylogger.info("list all ecs instances")
        request = DescribeInstancesRequest.DescribeInstancesRequest()
        request.set_PageNumber(1)
        request.set_PageSize(30)
        content = client.do_action_with_exception(request)
        response = json.loads(content.decode('utf-8'))
        mylogger.info("success! TotalCount = %s", response.get('TotalCount'))
        instances = response.get('Instances').get('Instance')
        for instance in instances:
            instance_name = instance.get('InstanceName')
            if instance_name.startswith('SdkIntegrationTestInstance'):
                create_time = int(instance_name[26:len(instance_name)])
                current_time = int(time.time())
                if create_time - current_time < 3600:
                    mylogger.info("found undeleted ecs instance(%s) but created in 60 minutes, try to delete next time"
                                  % instance_name)
                else:
                    mylogger.info("found undeleted ecs instance(%s), status=%s, try to delete it."
                                  % instance_name, instance['Status'])
                    if instance['Status'] == "Running":
                        # running -> stopped
                        TestEcsIntegration.stop_instance(client, instance['InstanceId'])
                    if instance['Status'] == "Stopped":
                        # stopped -> deleted
                        TestEcsIntegration.delete_instance(client, instance['InstanceId'])
                        # wait
                        TestEcsIntegration.wait_for_instance(client, instance['InstanceId'], 'Deleted')
