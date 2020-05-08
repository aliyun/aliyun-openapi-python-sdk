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
from aliyunsdkemr.endpoint import endpoint_data

class MetastoreCreateDatabaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'MetastoreCreateDatabase','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DbSource(self):
		return self.get_query_params().get('DbSource')

	def set_DbSource(self,DbSource):
		self.add_query_param('DbSource',DbSource)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_DataSourceId(self):
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceId(self,DataSourceId):
		self.add_query_param('DataSourceId',DataSourceId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)

	def get_LocationUri(self):
		return self.get_query_params().get('LocationUri')

	def set_LocationUri(self,LocationUri):
		self.add_query_param('LocationUri',LocationUri)

	def get_ClusterBizId(self):
		return self.get_query_params().get('ClusterBizId')

	def set_ClusterBizId(self,ClusterBizId):
		self.add_query_param('ClusterBizId',ClusterBizId)