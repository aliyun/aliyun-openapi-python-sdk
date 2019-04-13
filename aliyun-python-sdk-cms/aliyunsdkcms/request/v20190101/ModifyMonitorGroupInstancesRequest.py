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
class ModifyMonitorGroupInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyMonitorGroupInstances','cms')

	def get_Instancess(self):
		return self.get_query_params().get('Instancess')

	def set_Instancess(self,Instancess):
		for i in range(len(Instancess)):	
			if Instancess[i].get('InstanceId') is not None:
				self.add_query_param('Instances.' + str(i + 1) + '.InstanceId' , Instancess[i].get('InstanceId'))
			if Instancess[i].get('InstanceName') is not None:
				self.add_query_param('Instances.' + str(i + 1) + '.InstanceName' , Instancess[i].get('InstanceName'))
			if Instancess[i].get('RegionId') is not None:
				self.add_query_param('Instances.' + str(i + 1) + '.RegionId' , Instancess[i].get('RegionId'))
			if Instancess[i].get('Category') is not None:
				self.add_query_param('Instances.' + str(i + 1) + '.Category' , Instancess[i].get('Category'))


	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)