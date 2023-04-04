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
from aliyunsdkimm.endpoint import endpoint_data
import json

class CreateTriggerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateTrigger','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Notification(self): # Struct
		return self.get_body_params().get('Notification')

	def set_Notification(self, Notification):  # Struct
		self.add_body_params("Notification", json.dumps(Notification))
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_Tags(self): # Map
		return self.get_body_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_body_params("Tags", json.dumps(Tags))
	def get_Input(self): # Struct
		return self.get_body_params().get('Input')

	def set_Input(self, Input):  # Struct
		self.add_body_params("Input", json.dumps(Input))
	def get_ServiceRole(self): # String
		return self.get_body_params().get('ServiceRole')

	def set_ServiceRole(self, ServiceRole):  # String
		self.add_body_params('ServiceRole', ServiceRole)
	def get_Actions(self): # Array
		return self.get_body_params().get('Actions')

	def set_Actions(self, Actions):  # Array
		self.add_body_params("Actions", json.dumps(Actions))
