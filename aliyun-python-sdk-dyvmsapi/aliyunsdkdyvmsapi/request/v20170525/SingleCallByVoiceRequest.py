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
class SingleCallByVoiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'SingleCallByVoice')

	def get_Volume(self):
		return self.get_query_params().get('Volume')

	def set_Volume(self,Volume):
		self.add_query_param('Volume',Volume)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_VoiceCode(self):
		return self.get_query_params().get('VoiceCode')

	def set_VoiceCode(self,VoiceCode):
		self.add_query_param('VoiceCode',VoiceCode)

	def get_CalledShowNumber(self):
		return self.get_query_params().get('CalledShowNumber')

	def set_CalledShowNumber(self,CalledShowNumber):
		self.add_query_param('CalledShowNumber',CalledShowNumber)

	def get_PlayTimes(self):
		return self.get_query_params().get('PlayTimes')

	def set_PlayTimes(self,PlayTimes):
		self.add_query_param('PlayTimes',PlayTimes)

	def get_OutId(self):
		return self.get_query_params().get('OutId')

	def set_OutId(self,OutId):
		self.add_query_param('OutId',OutId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Speed(self):
		return self.get_query_params().get('Speed')

	def set_Speed(self,Speed):
		self.add_query_param('Speed',Speed)