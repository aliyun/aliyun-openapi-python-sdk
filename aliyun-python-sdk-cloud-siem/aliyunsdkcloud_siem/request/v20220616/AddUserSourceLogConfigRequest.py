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

class AddUserSourceLogConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'AddUserSourceLogConfig','cloud-siem')
		self.set_method('POST')

	def get_DisPlayLine(self): # String
		return self.get_body_params().get('DisPlayLine')

	def set_DisPlayLine(self, DisPlayLine):  # String
		self.add_body_params('DisPlayLine', DisPlayLine)
	def get_SubUserId(self): # Long
		return self.get_body_params().get('SubUserId')

	def set_SubUserId(self, SubUserId):  # Long
		self.add_body_params('SubUserId', SubUserId)
	def get_SourceProdCode(self): # String
		return self.get_body_params().get('SourceProdCode')

	def set_SourceProdCode(self, SourceProdCode):  # String
		self.add_body_params('SourceProdCode', SourceProdCode)
	def get_SourceLogInfo(self): # String
		return self.get_body_params().get('SourceLogInfo')

	def set_SourceLogInfo(self, SourceLogInfo):  # String
		self.add_body_params('SourceLogInfo', SourceLogInfo)
	def get_Deleted(self): # Integer
		return self.get_body_params().get('Deleted')

	def set_Deleted(self, Deleted):  # Integer
		self.add_body_params('Deleted', Deleted)
	def get_SourceLogCode(self): # String
		return self.get_body_params().get('SourceLogCode')

	def set_SourceLogCode(self, SourceLogCode):  # String
		self.add_body_params('SourceLogCode', SourceLogCode)
