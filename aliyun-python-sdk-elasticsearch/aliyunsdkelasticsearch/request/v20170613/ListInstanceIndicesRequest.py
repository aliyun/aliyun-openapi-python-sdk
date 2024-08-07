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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkelasticsearch.endpoint import endpoint_data

class ListInstanceIndicesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListInstanceIndices','elasticsearch')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/indices')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_all(self): # Boolean
		return self.get_query_params().get('all')

	def set_all(self, all):  # Boolean
		self.add_query_param('all', all)
	def get_InstanceId(self): # String
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_path_param('InstanceId', InstanceId)
	def get_isManaged(self): # Boolean
		return self.get_query_params().get('isManaged')

	def set_isManaged(self, isManaged):  # Boolean
		self.add_query_param('isManaged', isManaged)
	def get_size(self): # Integer
		return self.get_query_params().get('size')

	def set_size(self, size):  # Integer
		self.add_query_param('size', size)
	def get_name(self): # String
		return self.get_query_params().get('name')

	def set_name(self, name):  # String
		self.add_query_param('name', name)
	def get_page(self): # Integer
		return self.get_query_params().get('page')

	def set_page(self, page):  # Integer
		self.add_query_param('page', page)
	def get_isOpenstore(self): # Boolean
		return self.get_query_params().get('isOpenstore')

	def set_isOpenstore(self, isOpenstore):  # Boolean
		self.add_query_param('isOpenstore', isOpenstore)
