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

class UploadIoTDataToBlockchainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lto', '2021-07-07', 'UploadIoTDataToBlockchain')
		self.set_method('POST')

	def get_IotIdSource(self): # String
		return self.get_query_params().get('IotIdSource')

	def set_IotIdSource(self, IotIdSource):  # String
		self.add_query_param('IotIdSource', IotIdSource)
	def get_IotDataToken(self): # String
		return self.get_query_params().get('IotDataToken')

	def set_IotDataToken(self, IotDataToken):  # String
		self.add_query_param('IotDataToken', IotDataToken)
	def get_PrivacyData(self): # String
		return self.get_query_params().get('PrivacyData')

	def set_PrivacyData(self, PrivacyData):  # String
		self.add_query_param('PrivacyData', PrivacyData)
	def get_IotId(self): # String
		return self.get_query_params().get('IotId')

	def set_IotId(self, IotId):  # String
		self.add_query_param('IotId', IotId)
	def get_IotDataDigest(self): # String
		return self.get_query_params().get('IotDataDigest')

	def set_IotDataDigest(self, IotDataDigest):  # String
		self.add_query_param('IotDataDigest', IotDataDigest)
	def get_IotDataDID(self): # String
		return self.get_query_params().get('IotDataDID')

	def set_IotDataDID(self, IotDataDID):  # String
		self.add_query_param('IotDataDID', IotDataDID)
	def get_PlainData(self): # String
		return self.get_query_params().get('PlainData')

	def set_PlainData(self, PlainData):  # String
		self.add_query_param('PlainData', PlainData)
	def get_IotAuthType(self): # String
		return self.get_query_params().get('IotAuthType')

	def set_IotAuthType(self, IotAuthType):  # String
		self.add_query_param('IotAuthType', IotAuthType)
	def get_IotIdServiceProvider(self): # String
		return self.get_query_params().get('IotIdServiceProvider')

	def set_IotIdServiceProvider(self, IotIdServiceProvider):  # String
		self.add_query_param('IotIdServiceProvider', IotIdServiceProvider)
