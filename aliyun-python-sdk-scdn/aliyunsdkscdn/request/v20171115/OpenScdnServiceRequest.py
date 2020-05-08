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
from aliyunsdkscdn.endpoint import endpoint_data

class OpenScdnServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scdn', '2017-11-15', 'OpenScdnService')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StartDate(self):
		return self.get_query_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_query_param('StartDate',StartDate)

	def get_CcProtection(self):
		return self.get_query_params().get('CcProtection')

	def set_CcProtection(self,CcProtection):
		self.add_query_param('CcProtection',CcProtection)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_ProtectType(self):
		return self.get_query_params().get('ProtectType')

	def set_ProtectType(self,ProtectType):
		self.add_query_param('ProtectType',ProtectType)

	def get_DDoSBasic(self):
		return self.get_query_params().get('DDoSBasic')

	def set_DDoSBasic(self,DDoSBasic):
		self.add_query_param('DDoSBasic',DDoSBasic)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_DomainCount(self):
		return self.get_query_params().get('DomainCount')

	def set_DomainCount(self,DomainCount):
		self.add_query_param('DomainCount',DomainCount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_EndDate(self):
		return self.get_query_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_query_param('EndDate',EndDate)

	def get_ElasticProtection(self):
		return self.get_query_params().get('ElasticProtection')

	def set_ElasticProtection(self,ElasticProtection):
		self.add_query_param('ElasticProtection',ElasticProtection)