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
from aliyunsdknas.endpoint import endpoint_data

class CreateLifecyclePolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateLifecyclePolicy','nas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StorageType(self):
		return self.get_query_params().get('StorageType')

	def set_StorageType(self,StorageType):
		self.add_query_param('StorageType',StorageType)

	def get_Path(self):
		return self.get_query_params().get('Path')

	def set_Path(self,Path):
		self.add_query_param('Path',Path)

	def get_LifecyclePolicyName(self):
		return self.get_query_params().get('LifecyclePolicyName')

	def set_LifecyclePolicyName(self,LifecyclePolicyName):
		self.add_query_param('LifecyclePolicyName',LifecyclePolicyName)

	def get_FileSystemId(self):
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self,FileSystemId):
		self.add_query_param('FileSystemId',FileSystemId)

	def get_LifecycleRuleName(self):
		return self.get_query_params().get('LifecycleRuleName')

	def set_LifecycleRuleName(self,LifecycleRuleName):
		self.add_query_param('LifecycleRuleName',LifecycleRuleName)

	def get_Pathss(self):
		return self.get_query_params().get('Paths')

	def set_Pathss(self, Pathss):
		for depth1 in range(len(Pathss)):
			if Pathss[depth1] is not None:
				self.add_query_param('Paths.' + str(depth1 + 1) , Pathss[depth1])