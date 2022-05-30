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
from aliyunsdkarms.endpoint import endpoint_data

class CreateOrUpdateEventBridgeIntegrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateOrUpdateEventBridgeIntegration','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccessSecret(self): # String
		return self.get_body_params().get('AccessSecret')

	def set_AccessSecret(self, AccessSecret):  # String
		self.add_body_params('AccessSecret', AccessSecret)
	def get_EventBusRegionId(self): # String
		return self.get_body_params().get('EventBusRegionId')

	def set_EventBusRegionId(self, EventBusRegionId):  # String
		self.add_body_params('EventBusRegionId', EventBusRegionId)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Source(self): # String
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_body_params('Source', Source)
	def get_EventBusName(self): # String
		return self.get_body_params().get('EventBusName')

	def set_EventBusName(self, EventBusName):  # String
		self.add_body_params('EventBusName', EventBusName)
	def get_Endpoint(self): # String
		return self.get_body_params().get('Endpoint')

	def set_Endpoint(self, Endpoint):  # String
		self.add_body_params('Endpoint', Endpoint)
	def get_AccessKey(self): # String
		return self.get_body_params().get('AccessKey')

	def set_AccessKey(self, AccessKey):  # String
		self.add_body_params('AccessKey', AccessKey)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Id(self): # Long
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_body_params('Id', Id)
