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

from aliyunsdkcore.request import RpcRequest


class DescribeCommitContainerTaskRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, "Eci", "2018-08-08", "DescribeCommitContainerTask", "eci")

    def set_ContainerGroupId(self, ContainerGroupId):
        self.add_query_param("ContainerGroupId", ContainerGroupId)

    def get_ContainerGroupId(self):
        return self.get_query_params().get("ContainerGroupId")

    def set_TaskStatus(self, TaskStatus):
        self.add_query_param("TaskStatus", TaskStatus)

    def get_TaskStatus(self):
        return self.get_query_params().get("TaskStatus")

    def set_MaxResults(self, MaxResults):
        self.add_query_param("MaxResults", MaxResults)

    def get_MaxResults(self):
        return self.get_query_params().get("MaxResults")

    def set_NextToken(self, NextToken):
        self.add_query_param("NextToken", NextToken)

    def get_NextToken(self):
        return self.get_query_params().get("NextToken")

    def set_TaskId(self, TaskId):
        for i in range(len(TaskId)):
            self.add_query_param("TaskId." + str(i + 1), TaskId[i])
