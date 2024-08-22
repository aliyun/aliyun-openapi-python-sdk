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

class RiskEventSyncRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'RiskEventSync')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Submitter(self): # String
		return self.get_body_params().get('Submitter')

	def set_Submitter(self, Submitter):  # String
		self.add_body_params('Submitter', Submitter)
	def get_RiskDetail(self): # String
		return self.get_body_params().get('RiskDetail')

	def set_RiskDetail(self, RiskDetail):  # String
		self.add_body_params('RiskDetail', RiskDetail)
	def get_RiskType(self): # String
		return self.get_body_params().get('RiskType')

	def set_RiskType(self, RiskType):  # String
		self.add_body_params('RiskType', RiskType)
	def get_EventNumber(self): # String
		return self.get_body_params().get('EventNumber')

	def set_EventNumber(self, EventNumber):  # String
		self.add_body_params('EventNumber', EventNumber)
	def get_RiskEffectType(self): # String
		return self.get_body_params().get('RiskEffectType')

	def set_RiskEffectType(self, RiskEffectType):  # String
		self.add_body_params('RiskEffectType', RiskEffectType)
	def get_Deleted(self): # Boolean
		return self.get_body_params().get('Deleted')

	def set_Deleted(self, Deleted):  # Boolean
		self.add_body_params('Deleted', Deleted)
	def get_RelevanceBu(self): # String
		return self.get_body_params().get('RelevanceBu')

	def set_RelevanceBu(self, RelevanceBu):  # String
		self.add_body_params('RelevanceBu', RelevanceBu)
	def get_Source(self): # String
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_body_params('Source', Source)
	def get_RiskLevel(self): # String
		return self.get_body_params().get('RiskLevel')

	def set_RiskLevel(self, RiskLevel):  # String
		self.add_body_params('RiskLevel', RiskLevel)
	def get_EventName(self): # String
		return self.get_body_params().get('EventName')

	def set_EventName(self, EventName):  # String
		self.add_body_params('EventName', EventName)
	def get_DiscoveryTime(self): # Long
		return self.get_body_params().get('DiscoveryTime')

	def set_DiscoveryTime(self, DiscoveryTime):  # Long
		self.add_body_params('DiscoveryTime', DiscoveryTime)
