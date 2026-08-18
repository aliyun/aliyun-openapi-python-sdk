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

class CreateQosPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DFS', '2018-06-20', 'CreateQosPolicy','alidfs')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_FlowIds(self): # Array
		return self.get_query_params().get('FlowIds')

	def set_FlowIds(self, FlowIds):  # Array
		self.add_query_param("FlowIds", json.dumps(FlowIds))
	def get_ZoneIds(self): # Array
		return self.get_query_params().get('ZoneIds')

	def set_ZoneIds(self, ZoneIds):  # Array
		self.add_query_param("ZoneIds", json.dumps(ZoneIds))
	def get_MaxIOps(self): # Long
		return self.get_query_params().get('MaxIOps')

	def set_MaxIOps(self, MaxIOps):  # Long
		self.add_query_param('MaxIOps', MaxIOps)
	def get_InputRegionId(self): # String
		return self.get_query_params().get('InputRegionId')

	def set_InputRegionId(self, InputRegionId):  # String
		self.add_query_param('InputRegionId', InputRegionId)
	def get_MaxMetaQps(self): # Long
		return self.get_query_params().get('MaxMetaQps')

	def set_MaxMetaQps(self, MaxMetaQps):  # Long
		self.add_query_param('MaxMetaQps', MaxMetaQps)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_MaxIOBandWidth(self): # Long
		return self.get_query_params().get('MaxIOBandWidth')

	def set_MaxIOBandWidth(self, MaxIOBandWidth):  # Long
		self.add_query_param('MaxIOBandWidth', MaxIOBandWidth)
	def get_FederationId(self): # String
		return self.get_query_params().get('FederationId')

	def set_FederationId(self, FederationId):  # String
		self.add_query_param('FederationId', FederationId)
