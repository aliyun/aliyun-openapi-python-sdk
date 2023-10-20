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

class ModifyClientConfStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyClientConfStrategy','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_Tag(self): # String
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_query_param('Tag', Tag)
	def get_TagValue(self): # String
		return self.get_query_params().get('TagValue')

	def set_TagValue(self, TagValue):  # String
		self.add_query_param('TagValue', TagValue)
	def get_TagExt(self): # String
		return self.get_query_params().get('TagExt')

	def set_TagExt(self, TagExt):  # String
		self.add_query_param('TagExt', TagExt)
	def get_Uuidss(self): # RepeatList
		return self.get_query_params().get('Uuids')

	def set_Uuidss(self, Uuids):  # RepeatList
		for depth1 in range(len(Uuids)):
			self.add_query_param('Uuids.' + str(depth1 + 1), Uuids[depth1])
