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

class OperateBatchDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'OperateBatchDomain','alidns')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DomainRecordInfos(self):
		return self.get_query_params().get('DomainRecordInfos')

	def set_DomainRecordInfos(self,DomainRecordInfos):
		for i in range(len(DomainRecordInfos)):	
			if DomainRecordInfos[i].get('Rr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Rr' , DomainRecordInfos[i].get('Rr'))
			if DomainRecordInfos[i].get('NewType') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.NewType' , DomainRecordInfos[i].get('NewType'))
			if DomainRecordInfos[i].get('NewValue') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.NewValue' , DomainRecordInfos[i].get('NewValue'))
			if DomainRecordInfos[i].get('Line') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Line' , DomainRecordInfos[i].get('Line'))
			if DomainRecordInfos[i].get('Domain') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Domain' , DomainRecordInfos[i].get('Domain'))
			if DomainRecordInfos[i].get('Type') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Type' , DomainRecordInfos[i].get('Type'))
			if DomainRecordInfos[i].get('Priority') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Priority' , DomainRecordInfos[i].get('Priority'))
			if DomainRecordInfos[i].get('Value') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Value' , DomainRecordInfos[i].get('Value'))
			if DomainRecordInfos[i].get('Ttl') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.Ttl' , DomainRecordInfos[i].get('Ttl'))
			if DomainRecordInfos[i].get('NewRr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(i + 1) + '.NewRr' , DomainRecordInfos[i].get('NewRr'))


	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)