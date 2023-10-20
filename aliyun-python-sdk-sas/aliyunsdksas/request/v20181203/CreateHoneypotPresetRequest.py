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
from aliyunsdksas.endpoint import endpoint_data

class CreateHoneypotPresetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateHoneypotPreset','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_NodeId(self): # String
		return self.get_query_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_query_param('NodeId', NodeId)
	def get_PresetName(self): # String
		return self.get_query_params().get('PresetName')

	def set_PresetName(self, PresetName):  # String
		self.add_query_param('PresetName', PresetName)
	def get_Meta(self): # String
		return self.get_query_params().get('Meta')

	def set_Meta(self, Meta):  # String
		self.add_query_param('Meta', Meta)
	def get_HoneypotImageName(self): # String
		return self.get_query_params().get('HoneypotImageName')

	def set_HoneypotImageName(self, HoneypotImageName):  # String
		self.add_query_param('HoneypotImageName', HoneypotImageName)
