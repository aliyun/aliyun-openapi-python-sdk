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

class CreateWorkitemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rdc', '2018-08-21', 'CreateWorkitem','rdc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Author(self):
		return self.get_body_params().get('Author')

	def set_Author(self,Author):
		self.add_body_params('Author', Author)

	def get_Subject(self):
		return self.get_body_params().get('Subject')

	def set_Subject(self,Subject):
		self.add_body_params('Subject', Subject)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Stamp(self):
		return self.get_body_params().get('Stamp')

	def set_Stamp(self,Stamp):
		self.add_body_params('Stamp', Stamp)

	def get_AKProjectId(self):
		return self.get_body_params().get('AKProjectId')

	def set_AKProjectId(self,AKProjectId):
		self.add_body_params('AKProjectId', AKProjectId)

	def get_TemplateId(self):
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_body_params('TemplateId', TemplateId)

	def get_AssignedTo(self):
		return self.get_body_params().get('AssignedTo')

	def set_AssignedTo(self,AssignedTo):
		self.add_body_params('AssignedTo', AssignedTo)

	def get_PriorityId(self):
		return self.get_body_params().get('PriorityId')

	def set_PriorityId(self,PriorityId):
		self.add_body_params('PriorityId', PriorityId)

	def get_SeriousLevelId(self):
		return self.get_body_params().get('SeriousLevelId')

	def set_SeriousLevelId(self,SeriousLevelId):
		self.add_body_params('SeriousLevelId', SeriousLevelId)

	def get_ModuleIds(self):
		return self.get_body_params().get('ModuleIds')

	def set_ModuleIds(self,ModuleIds):
		self.add_body_params('ModuleIds', ModuleIds)

	def get_CorpIdentifier(self):
		return self.get_query_params().get('CorpIdentifier')

	def set_CorpIdentifier(self,CorpIdentifier):
		self.add_query_param('CorpIdentifier',CorpIdentifier)

	def get_WatcherUsers(self):
		return self.get_body_params().get('WatcherUsers')

	def set_WatcherUsers(self,WatcherUsers):
		self.add_body_params('WatcherUsers', WatcherUsers)

	def get_Verifier(self):
		return self.get_body_params().get('Verifier')

	def set_Verifier(self,Verifier):
		self.add_body_params('Verifier', Verifier)

	def get_CfList(self):
		return self.get_body_params().get('CfList')

	def set_CfList(self,CfList):
		self.add_body_params('CfList', CfList)