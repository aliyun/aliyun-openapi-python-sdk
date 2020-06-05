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

class DiffFlowEntitySnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'DiffFlowEntitySnapshot','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SrcRevision(self):
		return self.get_query_params().get('SrcRevision')

	def set_SrcRevision(self,SrcRevision):
		self.add_query_param('SrcRevision',SrcRevision)

	def get_EntityId(self):
		return self.get_query_params().get('EntityId')

	def set_EntityId(self,EntityId):
		self.add_query_param('EntityId',EntityId)

	def get_DstRevision(self):
		return self.get_query_params().get('DstRevision')

	def set_DstRevision(self,DstRevision):
		self.add_query_param('DstRevision',DstRevision)

	def get_EntityType(self):
		return self.get_query_params().get('EntityType')

	def set_EntityType(self,EntityType):
		self.add_query_param('EntityType',EntityType)