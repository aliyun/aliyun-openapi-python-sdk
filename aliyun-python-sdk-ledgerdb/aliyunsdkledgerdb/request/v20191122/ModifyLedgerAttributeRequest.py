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

class ModifyLedgerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ledgerdb', '2019-11-22', 'ModifyLedgerAttribute','ledgerdb')
		self.set_method('POST')

	def get_LedgerId(self):
		return self.get_body_params().get('LedgerId')

	def set_LedgerId(self,LedgerId):
		self.add_body_params('LedgerId', LedgerId)

	def get_LedgerName(self):
		return self.get_body_params().get('LedgerName')

	def set_LedgerName(self,LedgerName):
		self.add_body_params('LedgerName', LedgerName)

	def get_LedgerDescription(self):
		return self.get_body_params().get('LedgerDescription')

	def set_LedgerDescription(self,LedgerDescription):
		self.add_body_params('LedgerDescription', LedgerDescription)