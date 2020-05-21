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
from aliyunsdkfnf.endpoint import endpoint_data

class CreateFlowRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'fnf', '2019-03-15', 'CreateFlow')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_RoleArn(self):
		return self.get_body_params().get('RoleArn')

	def set_RoleArn(self,RoleArn):
		self.add_body_params('RoleArn', RoleArn)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_Definition(self):
		return self.get_body_params().get('Definition')

	def set_Definition(self,Definition):
		self.add_body_params('Definition', Definition)

	def get_ExternalStorageLocation(self):
		return self.get_body_params().get('ExternalStorageLocation')

	def set_ExternalStorageLocation(self,ExternalStorageLocation):
		self.add_body_params('ExternalStorageLocation', ExternalStorageLocation)