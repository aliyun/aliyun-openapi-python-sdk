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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class ListMetaCollectionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListMetaCollections')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Creator(self): # String
		return self.get_query_params().get('Creator')

	def set_Creator(self, Creator):  # String
		self.add_query_param('Creator', Creator)
	def get_Follower(self): # String
		return self.get_query_params().get('Follower')

	def set_Follower(self, Follower):  # String
		self.add_query_param('Follower', Follower)
	def get_ParentQualifiedName(self): # String
		return self.get_query_params().get('ParentQualifiedName')

	def set_ParentQualifiedName(self, ParentQualifiedName):  # String
		self.add_query_param('ParentQualifiedName', ParentQualifiedName)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_CollectionType(self): # String
		return self.get_query_params().get('CollectionType')

	def set_CollectionType(self, CollectionType):  # String
		self.add_query_param('CollectionType', CollectionType)
	def get_Administrator(self): # String
		return self.get_query_params().get('Administrator')

	def set_Administrator(self, Administrator):  # String
		self.add_query_param('Administrator', Administrator)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
