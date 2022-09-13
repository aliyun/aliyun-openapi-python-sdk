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

class UpdateBatchOperateCardsTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'UpdateBatchOperateCardsTask','fivegcc')
		self.set_method('POST')

	def get_Iccids(self): # Array
		return self.get_query_params().get('Iccids')

	def set_Iccids(self, Iccids):  # Array
		for index1, value1 in enumerate(Iccids):
			self.add_query_param('Iccids.' + str(index1 + 1), value1)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Threshold(self): # Long
		return self.get_query_params().get('Threshold')

	def set_Threshold(self, Threshold):  # Long
		self.add_query_param('Threshold', Threshold)
	def get_BatchOperateCardsTaskId(self): # String
		return self.get_query_params().get('BatchOperateCardsTaskId')

	def set_BatchOperateCardsTaskId(self, BatchOperateCardsTaskId):  # String
		self.add_query_param('BatchOperateCardsTaskId', BatchOperateCardsTaskId)
	def get_EffectType(self): # String
		return self.get_query_params().get('EffectType')

	def set_EffectType(self, EffectType):  # String
		self.add_query_param('EffectType', EffectType)
	def get_WirelessCloudConnectorIds(self): # Array
		return self.get_query_params().get('WirelessCloudConnectorIds')

	def set_WirelessCloudConnectorIds(self, WirelessCloudConnectorIds):  # Array
		for index1, value1 in enumerate(WirelessCloudConnectorIds):
			self.add_query_param('WirelessCloudConnectorIds.' + str(index1 + 1), value1)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_OperateType(self): # String
		return self.get_query_params().get('OperateType')

	def set_OperateType(self, OperateType):  # String
		self.add_query_param('OperateType', OperateType)
	def get_IccidsOssFilePath(self): # String
		return self.get_query_params().get('IccidsOssFilePath')

	def set_IccidsOssFilePath(self, IccidsOssFilePath):  # String
		self.add_query_param('IccidsOssFilePath', IccidsOssFilePath)
