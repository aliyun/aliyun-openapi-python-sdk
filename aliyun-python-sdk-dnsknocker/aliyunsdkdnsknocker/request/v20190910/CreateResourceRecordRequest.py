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
from aliyunsdkdnsknocker.endpoint import endpoint_data

class CreateResourceRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DnsKnocker', '2019-09-10', 'CreateResourceRecord','dns_knocker')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AccessID(self):
		return self.get_body_params().get('AccessID')

	def set_AccessID(self,AccessID):
		self.add_body_params('AccessID', AccessID)

	def get_RrTTL(self):
		return self.get_body_params().get('RrTTL')

	def set_RrTTL(self,RrTTL):
		self.add_body_params('RrTTL', RrTTL)

	def get_AccessSecret(self):
		return self.get_body_params().get('AccessSecret')

	def set_AccessSecret(self,AccessSecret):
		self.add_body_params('AccessSecret', AccessSecret)

	def get_RrLine(self):
		return self.get_body_params().get('RrLine')

	def set_RrLine(self,RrLine):
		self.add_body_params('RrLine', RrLine)

	def get_DomainName(self):
		return self.get_body_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_body_params('DomainName', DomainName)

	def get_RrValue(self):
		return self.get_body_params().get('RrValue')

	def set_RrValue(self,RrValue):
		self.add_body_params('RrValue', RrValue)

	def get_ZoneName(self):
		return self.get_body_params().get('ZoneName')

	def set_ZoneName(self,ZoneName):
		self.add_body_params('ZoneName', ZoneName)

	def get_TransactionId(self):
		return self.get_body_params().get('TransactionId')

	def set_TransactionId(self,TransactionId):
		self.add_body_params('TransactionId', TransactionId)

	def get_Group(self):
		return self.get_body_params().get('Group')

	def set_Group(self,Group):
		self.add_body_params('Group', Group)

	def get_RrType(self):
		return self.get_body_params().get('RrType')

	def set_RrType(self,RrType):
		self.add_body_params('RrType', RrType)