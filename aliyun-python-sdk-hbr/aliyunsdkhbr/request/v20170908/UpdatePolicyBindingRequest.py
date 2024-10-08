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
from aliyunsdkhbr.endpoint import endpoint_data
import json

class UpdatePolicyBindingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdatePolicyBinding','hbr')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_PolicyId(self): # String
		return self.get_body_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_body_params('PolicyId', PolicyId)
	def get_PolicyBindingDescription(self): # String
		return self.get_query_params().get('PolicyBindingDescription')

	def set_PolicyBindingDescription(self, PolicyBindingDescription):  # String
		self.add_query_param('PolicyBindingDescription', PolicyBindingDescription)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Disabled(self): # Boolean
		return self.get_query_params().get('Disabled')

	def set_Disabled(self, Disabled):  # Boolean
		self.add_query_param('Disabled', Disabled)
	def get_Exclude(self): # String
		return self.get_query_params().get('Exclude')

	def set_Exclude(self, Exclude):  # String
		self.add_query_param('Exclude', Exclude)
	def get_AdvancedOptions(self): # Struct
		return self.get_query_params().get('AdvancedOptions')

	def set_AdvancedOptions(self, AdvancedOptions):  # Struct
		self.add_query_param("AdvancedOptions", json.dumps(AdvancedOptions))
	def get_Include(self): # String
		return self.get_query_params().get('Include')

	def set_Include(self, Include):  # String
		self.add_query_param('Include', Include)
	def get_SpeedLimit(self): # String
		return self.get_query_params().get('SpeedLimit')

	def set_SpeedLimit(self, SpeedLimit):  # String
		self.add_query_param('SpeedLimit', SpeedLimit)
	def get_DataSourceId(self): # String
		return self.get_body_params().get('DataSourceId')

	def set_DataSourceId(self, DataSourceId):  # String
		self.add_body_params('DataSourceId', DataSourceId)
