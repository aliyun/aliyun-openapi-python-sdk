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
import json

class CreateApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'CreateApplication','bpstudio')
		self.set_method('POST')

	def get_Variables(self): # Map
		return self.get_body_params().get('Variables')

	def set_Variables(self, Variables):  # Map
		self.add_body_params("Variables", json.dumps(Variables))
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_Instances(self): # Array
		return self.get_body_params().get('Instances')

	def set_Instances(self, Instances):  # Array
		self.add_body_params("Instances", json.dumps(Instances))
	def get_Configuration(self): # Map
		return self.get_body_params().get('Configuration')

	def set_Configuration(self, Configuration):  # Map
		self.add_body_params("Configuration", json.dumps(Configuration))
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_AreaId(self): # String
		return self.get_body_params().get('AreaId')

	def set_AreaId(self, AreaId):  # String
		self.add_body_params('AreaId', AreaId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
