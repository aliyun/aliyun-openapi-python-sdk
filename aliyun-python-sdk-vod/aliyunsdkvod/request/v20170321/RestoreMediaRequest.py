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
from aliyunsdkvod.endpoint import endpoint_data

class RestoreMediaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'RestoreMedia','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RestoreTier(self): # String
		return self.get_query_params().get('RestoreTier')

	def set_RestoreTier(self, RestoreTier):  # String
		self.add_query_param('RestoreTier', RestoreTier)
	def get_RestoreDays(self): # String
		return self.get_query_params().get('RestoreDays')

	def set_RestoreDays(self, RestoreDays):  # String
		self.add_query_param('RestoreDays', RestoreDays)
	def get_Scope(self): # String
		return self.get_query_params().get('Scope')

	def set_Scope(self, Scope):  # String
		self.add_query_param('Scope', Scope)
	def get_MediaIds(self): # String
		return self.get_query_params().get('MediaIds')

	def set_MediaIds(self, MediaIds):  # String
		self.add_query_param('MediaIds', MediaIds)
