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
from aliyunsdkoos.endpoint import endpoint_data
import json

class UpdateApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'UpdateApplication','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_AlarmConfig(self): # Struct
		return self.get_query_params().get('AlarmConfig')

	def set_AlarmConfig(self, AlarmConfig):  # Struct
		self.add_query_param("AlarmConfig", json.dumps(AlarmConfig))
	def get_DeleteAlarmRulesBeforeUpdate(self): # Boolean
		return self.get_query_params().get('DeleteAlarmRulesBeforeUpdate')

	def set_DeleteAlarmRulesBeforeUpdate(self, DeleteAlarmRulesBeforeUpdate):  # Boolean
		self.add_query_param('DeleteAlarmRulesBeforeUpdate', DeleteAlarmRulesBeforeUpdate)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
