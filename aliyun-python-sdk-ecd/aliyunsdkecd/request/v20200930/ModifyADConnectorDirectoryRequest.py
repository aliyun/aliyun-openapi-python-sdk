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
from aliyunsdkecd.endpoint import endpoint_data

class ModifyADConnectorDirectoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyADConnectorDirectory')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SubDomainDnsAddresss(self): # RepeatList
		return self.get_query_params().get('SubDomainDnsAddress')

	def set_SubDomainDnsAddresss(self, SubDomainDnsAddress):  # RepeatList
		for depth1 in range(len(SubDomainDnsAddress)):
			self.add_query_param('SubDomainDnsAddress.' + str(depth1 + 1), SubDomainDnsAddress[depth1])
	def get_SubDomainName(self): # String
		return self.get_query_params().get('SubDomainName')

	def set_SubDomainName(self, SubDomainName):  # String
		self.add_query_param('SubDomainName', SubDomainName)
	def get_DomainPassword(self): # String
		return self.get_query_params().get('DomainPassword')

	def set_DomainPassword(self, DomainPassword):  # String
		self.add_query_param('DomainPassword', DomainPassword)
	def get_DirectoryId(self): # String
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self, DirectoryId):  # String
		self.add_query_param('DirectoryId', DirectoryId)
	def get_AdHostname(self): # String
		return self.get_query_params().get('AdHostname')

	def set_AdHostname(self, AdHostname):  # String
		self.add_query_param('AdHostname', AdHostname)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_DirectoryName(self): # String
		return self.get_query_params().get('DirectoryName')

	def set_DirectoryName(self, DirectoryName):  # String
		self.add_query_param('DirectoryName', DirectoryName)
	def get_MfaEnabled(self): # Boolean
		return self.get_query_params().get('MfaEnabled')

	def set_MfaEnabled(self, MfaEnabled):  # Boolean
		self.add_query_param('MfaEnabled', MfaEnabled)
	def get_DomainUserName(self): # String
		return self.get_query_params().get('DomainUserName')

	def set_DomainUserName(self, DomainUserName):  # String
		self.add_query_param('DomainUserName', DomainUserName)
	def get_DnsAddresss(self): # RepeatList
		return self.get_query_params().get('DnsAddress')

	def set_DnsAddresss(self, DnsAddress):  # RepeatList
		for depth1 in range(len(DnsAddress)):
			self.add_query_param('DnsAddress.' + str(depth1 + 1), DnsAddress[depth1])
	def get_OUName(self): # String
		return self.get_query_params().get('OUName')

	def set_OUName(self, OUName):  # String
		self.add_query_param('OUName', OUName)
