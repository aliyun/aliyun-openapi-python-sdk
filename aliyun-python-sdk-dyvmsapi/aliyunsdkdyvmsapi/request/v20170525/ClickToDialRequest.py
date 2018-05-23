# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ClickToDialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'ClickToDial')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RecordFlag(self):
		return self.get_query_params().get('RecordFlag')

	def set_RecordFlag(self,RecordFlag):
		self.add_query_param('RecordFlag',RecordFlag)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CallerShowNumber(self):
		return self.get_query_params().get('CallerShowNumber')

	def set_CallerShowNumber(self,CallerShowNumber):
		self.add_query_param('CallerShowNumber',CallerShowNumber)

	def get_SessionTimeout(self):
		return self.get_query_params().get('SessionTimeout')

	def set_SessionTimeout(self,SessionTimeout):
		self.add_query_param('SessionTimeout',SessionTimeout)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_CalledShowNumber(self):
		return self.get_query_params().get('CalledShowNumber')

	def set_CalledShowNumber(self,CalledShowNumber):
		self.add_query_param('CalledShowNumber',CalledShowNumber)

	def get_OutId(self):
		return self.get_query_params().get('OutId')

	def set_OutId(self,OutId):
		self.add_query_param('OutId',OutId)

	def get_AsrFlag(self):
		return self.get_query_params().get('AsrFlag')

	def set_AsrFlag(self,AsrFlag):
		self.add_query_param('AsrFlag',AsrFlag)

	def get_AsrModelId(self):
		return self.get_query_params().get('AsrModelId')

	def set_AsrModelId(self,AsrModelId):
		self.add_query_param('AsrModelId',AsrModelId)

	def get_CallerNumber(self):
		return self.get_query_params().get('CallerNumber')

	def set_CallerNumber(self,CallerNumber):
		self.add_query_param('CallerNumber',CallerNumber)