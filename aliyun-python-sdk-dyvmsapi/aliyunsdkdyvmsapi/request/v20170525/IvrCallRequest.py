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
class IvrCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'IvrCall')

	def get_ByeCode(self):
		return self.get_query_params().get('ByeCode')

	def set_ByeCode(self,ByeCode):
		self.add_query_param('ByeCode',ByeCode)

	def get_MenuKeyMaps(self):
		return self.get_query_params().get('MenuKeyMaps')

	def set_MenuKeyMaps(self,MenuKeyMaps):
		for i in range(len(MenuKeyMaps)):	
			if MenuKeyMaps[i].get('Key') is not None:
				self.add_query_param('MenuKeyMap.' + str(i + 1) + '.Key' , MenuKeyMaps[i].get('Key'))
			if MenuKeyMaps[i].get('Code') is not None:
				self.add_query_param('MenuKeyMap.' + str(i + 1) + '.Code' , MenuKeyMaps[i].get('Code'))
			if MenuKeyMaps[i].get('TtsParams') is not None:
				self.add_query_param('MenuKeyMap.' + str(i + 1) + '.TtsParams' , MenuKeyMaps[i].get('TtsParams'))


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_StartTtsParams(self):
		return self.get_query_params().get('StartTtsParams')

	def set_StartTtsParams(self,StartTtsParams):
		self.add_query_param('StartTtsParams',StartTtsParams)

	def get_PlayTimes(self):
		return self.get_query_params().get('PlayTimes')

	def set_PlayTimes(self,PlayTimes):
		self.add_query_param('PlayTimes',PlayTimes)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Timeout(self):
		return self.get_query_params().get('Timeout')

	def set_Timeout(self,Timeout):
		self.add_query_param('Timeout',Timeout)

	def get_StartCode(self):
		return self.get_query_params().get('StartCode')

	def set_StartCode(self,StartCode):
		self.add_query_param('StartCode',StartCode)

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

	def get_ByeTtsParams(self):
		return self.get_query_params().get('ByeTtsParams')

	def set_ByeTtsParams(self,ByeTtsParams):
		self.add_query_param('ByeTtsParams',ByeTtsParams)