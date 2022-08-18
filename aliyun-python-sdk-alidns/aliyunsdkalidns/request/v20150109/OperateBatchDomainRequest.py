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
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DomainRecordInfos(self): # RepeatList
		return self.get_query_params().get('DomainRecordInfo')

	def set_DomainRecordInfos(self, DomainRecordInfo):  # RepeatList
		for depth1 in range(len(DomainRecordInfo)):
			if DomainRecordInfo[depth1].get('Rr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Rr', DomainRecordInfo[depth1].get('Rr'))
			if DomainRecordInfo[depth1].get('NewType') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewType', DomainRecordInfo[depth1].get('NewType'))
			if DomainRecordInfo[depth1].get('NewValue') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewValue', DomainRecordInfo[depth1].get('NewValue'))
			if DomainRecordInfo[depth1].get('Line') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Line', DomainRecordInfo[depth1].get('Line'))
			if DomainRecordInfo[depth1].get('Domain') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Domain', DomainRecordInfo[depth1].get('Domain'))
			if DomainRecordInfo[depth1].get('Type') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Type', DomainRecordInfo[depth1].get('Type'))
			if DomainRecordInfo[depth1].get('Priority') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Priority', DomainRecordInfo[depth1].get('Priority'))
			if DomainRecordInfo[depth1].get('Value') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Value', DomainRecordInfo[depth1].get('Value'))
			if DomainRecordInfo[depth1].get('Ttl') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Ttl', DomainRecordInfo[depth1].get('Ttl'))
			if DomainRecordInfo[depth1].get('NewRr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewRr', DomainRecordInfo[depth1].get('NewRr'))
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
