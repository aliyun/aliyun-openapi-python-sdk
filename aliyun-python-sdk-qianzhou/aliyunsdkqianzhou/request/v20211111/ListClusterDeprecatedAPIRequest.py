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

class ListClusterDeprecatedAPIRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'qianzhou', '2021-11-11', 'ListClusterDeprecatedAPI')
		self.set_uri_pattern('/popapi/listDeprecatedK8sAPI')
		self.set_method('POST')

	def get_cluster_id(self): # String
		return self.get_query_params().get('cluster_id')

	def set_cluster_id(self, cluster_id):  # String
		self.add_query_param('cluster_id', cluster_id)
	def get_page_no(self): # Integer
		return self.get_query_params().get('page_no')

	def set_page_no(self, page_no):  # Integer
		self.add_query_param('page_no', page_no)
	def get_target_version(self): # String
		return self.get_query_params().get('target_version')

	def set_target_version(self, target_version):  # String
		self.add_query_param('target_version', target_version)
	def get_page_size(self): # Integer
		return self.get_query_params().get('page_size')

	def set_page_size(self, page_size):  # Integer
		self.add_query_param('page_size', page_size)
