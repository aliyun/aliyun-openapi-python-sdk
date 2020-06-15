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
from aliyunsdkbaas.endpoint import endpoint_data

class UpdateAntChainContractContentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'UpdateAntChainContractContent')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_ParentContentId(self):
		return self.get_body_params().get('ParentContentId')

	def set_ParentContentId(self,ParentContentId):
		self.add_body_params('ParentContentId', ParentContentId)

	def get_ContentName(self):
		return self.get_body_params().get('ContentName')

	def set_ContentName(self,ContentName):
		self.add_body_params('ContentName', ContentName)

	def get_ContentId(self):
		return self.get_body_params().get('ContentId')

	def set_ContentId(self,ContentId):
		self.add_body_params('ContentId', ContentId)