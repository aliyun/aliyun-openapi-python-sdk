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
class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'CreateInstance','vipaegis')

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_IsAutoRenew(self):
		return self.get_query_params().get('IsAutoRenew')

	def set_IsAutoRenew(self,IsAutoRenew):
		self.add_query_param('IsAutoRenew',IsAutoRenew)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_VmNumber(self):
		return self.get_query_params().get('VmNumber')

	def set_VmNumber(self,VmNumber):
		self.add_query_param('VmNumber',VmNumber)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VersionCode(self):
		return self.get_query_params().get('VersionCode')

	def set_VersionCode(self,VersionCode):
		self.add_query_param('VersionCode',VersionCode)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)

	def get_AutoRenewDuration(self):
		return self.get_query_params().get('AutoRenewDuration')

	def set_AutoRenewDuration(self,AutoRenewDuration):
		self.add_query_param('AutoRenewDuration',AutoRenewDuration)