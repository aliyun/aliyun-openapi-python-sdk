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
from aliyunsdkiot.endpoint import endpoint_data

class InvokeThingsServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'InvokeThingsService','Iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Identifier(self):
		return self.get_query_params().get('Identifier')

	def set_Identifier(self,Identifier):
		self.add_query_param('Identifier',Identifier)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_Args(self):
		return self.get_query_params().get('Args')

	def set_Args(self,Args):
		self.add_query_param('Args',Args)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_DeviceNames(self):
		return self.get_query_params().get('DeviceNames')

	def set_DeviceNames(self,DeviceNames):
		for i in range(len(DeviceNames)):	
			if DeviceNames[i] is not None:
				self.add_query_param('DeviceName.' + str(i + 1) , DeviceNames[i]);