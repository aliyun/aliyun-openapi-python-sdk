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
from aliyunsdkedas.endpoint import endpoint_data

class InsertClusterMemberRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertClusterMember','Edas')
		self.set_uri_pattern('/pop/v5/resource/cluster_member')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_password(self):
		return self.get_query_params().get('password')

	def set_password(self,password):
		self.add_query_param('password',password)

	def get_instanceIds(self):
		return self.get_query_params().get('instanceIds')

	def set_instanceIds(self,instanceIds):
		self.add_query_param('instanceIds',instanceIds)

	def get_clusterId(self):
		return self.get_query_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_query_param('clusterId',clusterId)