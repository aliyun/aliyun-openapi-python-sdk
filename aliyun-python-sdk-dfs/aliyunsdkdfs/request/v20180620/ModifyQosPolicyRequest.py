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

class ModifyQosPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DFS', '2018-06-20', 'ModifyQosPolicy','alidfs')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_QosPolicyId(self): # String
		return self.get_query_params().get('QosPolicyId')

	def set_QosPolicyId(self, QosPolicyId):  # String
		self.add_query_param('QosPolicyId', QosPolicyId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
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
	def get_MaxIOBandWidth(self): # Long
		return self.get_query_params().get('MaxIOBandWidth')

	def set_MaxIOBandWidth(self, MaxIOBandWidth):  # Long
		self.add_query_param('MaxIOBandWidth', MaxIOBandWidth)
