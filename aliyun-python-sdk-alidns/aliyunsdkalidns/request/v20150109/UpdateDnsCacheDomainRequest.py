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
from aliyunsdkalidns.endpoint import endpoint_data

class UpdateDnsCacheDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateDnsCacheDomain','alidns')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceProtocol(self): # String
		return self.get_query_params().get('SourceProtocol')

	def set_SourceProtocol(self, SourceProtocol):  # String
		self.add_query_param('SourceProtocol', SourceProtocol)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_CacheTtlMax(self): # Integer
		return self.get_query_params().get('CacheTtlMax')

	def set_CacheTtlMax(self, CacheTtlMax):  # Integer
		self.add_query_param('CacheTtlMax', CacheTtlMax)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SourceEdns(self): # String
		return self.get_query_params().get('SourceEdns')

	def set_SourceEdns(self, SourceEdns):  # String
		self.add_query_param('SourceEdns', SourceEdns)
	def get_CacheTtlMin(self): # Integer
		return self.get_query_params().get('CacheTtlMin')

	def set_CacheTtlMin(self, CacheTtlMin):  # Integer
		self.add_query_param('CacheTtlMin', CacheTtlMin)
	def get_SourceDnsServers(self): # RepeatList
		return self.get_query_params().get('SourceDnsServer')

	def set_SourceDnsServers(self, SourceDnsServer):  # RepeatList
		for depth1 in range(len(SourceDnsServer)):
			if SourceDnsServer[depth1].get('Port') is not None:
				self.add_query_param('SourceDnsServer.' + str(depth1 + 1) + '.Port', SourceDnsServer[depth1].get('Port'))
			if SourceDnsServer[depth1].get('Host') is not None:
				self.add_query_param('SourceDnsServer.' + str(depth1 + 1) + '.Host', SourceDnsServer[depth1].get('Host'))
