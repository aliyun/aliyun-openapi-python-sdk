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
from aliyunsdkrdc.endpoint import endpoint_data

class SearchWorkitemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rdc', '2018-08-21', 'SearchWorkitem','rdc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SprintId(self):
		return self.get_body_params().get('SprintId')

	def set_SprintId(self,SprintId):
		self.add_body_params('SprintId', SprintId)

	def get_CorpIdentifier(self):
		return self.get_query_params().get('CorpIdentifier')

	def set_CorpIdentifier(self,CorpIdentifier):
		self.add_query_param('CorpIdentifier',CorpIdentifier)

	def get_ToPage(self):
		return self.get_body_params().get('ToPage')

	def set_ToPage(self,ToPage):
		self.add_body_params('ToPage', ToPage)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_Stamp(self):
		return self.get_body_params().get('Stamp')

	def set_Stamp(self,Stamp):
		self.add_body_params('Stamp', Stamp)

	def get_AKProjectId(self):
		return self.get_body_params().get('AKProjectId')

	def set_AKProjectId(self,AKProjectId):
		self.add_body_params('AKProjectId', AKProjectId)