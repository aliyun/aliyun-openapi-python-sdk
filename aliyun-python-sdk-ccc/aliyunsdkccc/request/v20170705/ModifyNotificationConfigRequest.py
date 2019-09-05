# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkccc.endpoint import endpoint_data

class ModifyNotificationConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'ModifyNotificationConfig')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Subscriptionss(self):
		return self.get_query_params().get('Subscriptionss')

	def set_Subscriptionss(self,Subscriptionss):
		for i in range(len(Subscriptionss)):	
			if Subscriptionss[i].get('DisplayName') is not None:
				self.add_query_param('Subscriptions.' + str(i + 1) + '.DisplayName' , Subscriptionss[i].get('DisplayName'))
			if Subscriptionss[i].get('Name') is not None:
				self.add_query_param('Subscriptions.' + str(i + 1) + '.Name' , Subscriptionss[i].get('Name'))
			if Subscriptionss[i].get('Selected') is not None:
				self.add_query_param('Subscriptions.' + str(i + 1) + '.Selected' , Subscriptionss[i].get('Selected'))


	def get_AccessPoint(self):
		return self.get_query_params().get('AccessPoint')

	def set_AccessPoint(self,AccessPoint):
		self.add_query_param('AccessPoint',AccessPoint)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Topic(self):
		return self.get_query_params().get('Topic')

	def set_Topic(self,Topic):
		self.add_query_param('Topic',Topic)

	def get_ProducerId(self):
		return self.get_query_params().get('ProducerId')

	def set_ProducerId(self,ProducerId):
		self.add_query_param('ProducerId',ProducerId)