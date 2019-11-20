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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class CreateRobotTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'CreateRobotTask','dyvms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RecallStateCodes(self):
		return self.get_query_params().get('RecallStateCodes')

	def set_RecallStateCodes(self,RecallStateCodes):
		self.add_query_param('RecallStateCodes',RecallStateCodes)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_RecallTimes(self):
		return self.get_query_params().get('RecallTimes')

	def set_RecallTimes(self,RecallTimes):
		self.add_query_param('RecallTimes',RecallTimes)

	def get_IsSelfLine(self):
		return self.get_query_params().get('IsSelfLine')

	def set_IsSelfLine(self,IsSelfLine):
		self.add_query_param('IsSelfLine',IsSelfLine)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RetryType(self):
		return self.get_query_params().get('RetryType')

	def set_RetryType(self,RetryType):
		self.add_query_param('RetryType',RetryType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DialogId(self):
		return self.get_query_params().get('DialogId')

	def set_DialogId(self,DialogId):
		self.add_query_param('DialogId',DialogId)

	def get_Caller(self):
		return self.get_query_params().get('Caller')

	def set_Caller(self,Caller):
		self.add_query_param('Caller',Caller)

	def get_NumberStatusIdent(self):
		return self.get_query_params().get('NumberStatusIdent')

	def set_NumberStatusIdent(self,NumberStatusIdent):
		self.add_query_param('NumberStatusIdent',NumberStatusIdent)

	def get_CorpName(self):
		return self.get_query_params().get('CorpName')

	def set_CorpName(self,CorpName):
		self.add_query_param('CorpName',CorpName)

	def get_RecallInterval(self):
		return self.get_query_params().get('RecallInterval')

	def set_RecallInterval(self,RecallInterval):
		self.add_query_param('RecallInterval',RecallInterval)