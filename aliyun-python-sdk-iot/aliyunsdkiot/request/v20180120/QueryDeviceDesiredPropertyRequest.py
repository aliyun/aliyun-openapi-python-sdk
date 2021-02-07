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

class QueryDeviceDesiredPropertyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'QueryDeviceDesiredProperty','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IotId(self):
		return self.get_query_params().get('IotId')

	def set_IotId(self,IotId):
		self.add_query_param('IotId',IotId)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_Identifiers(self):
		return self.get_query_params().get('Identifier')

	def set_Identifiers(self, Identifiers):
		for depth1 in range(len(Identifiers)):
			if Identifiers[depth1] is not None:
				self.add_query_param('Identifier.' + str(depth1 + 1) , Identifiers[depth1])

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_DeviceName(self):
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_query_param('DeviceName',DeviceName)

	def get_FunctionBlockId(self):
		return self.get_query_params().get('FunctionBlockId')

	def set_FunctionBlockId(self,FunctionBlockId):
		self.add_query_param('FunctionBlockId',FunctionBlockId)