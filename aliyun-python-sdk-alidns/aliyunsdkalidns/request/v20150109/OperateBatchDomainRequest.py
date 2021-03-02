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

class OperateBatchDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'OperateBatchDomain','alidns')
		self.set_method('POST')

	def get_DomainRecordInfos(self):
		return self.get_query_params().get('DomainRecordInfo')

	def set_DomainRecordInfos(self, DomainRecordInfos):
		for depth1 in range(len(DomainRecordInfos)):
			if DomainRecordInfos[depth1].get('Rr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Rr', DomainRecordInfos[depth1].get('Rr'))
			if DomainRecordInfos[depth1].get('NewType') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewType', DomainRecordInfos[depth1].get('NewType'))
			if DomainRecordInfos[depth1].get('NewValue') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewValue', DomainRecordInfos[depth1].get('NewValue'))
			if DomainRecordInfos[depth1].get('Line') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Line', DomainRecordInfos[depth1].get('Line'))
			if DomainRecordInfos[depth1].get('Domain') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Domain', DomainRecordInfos[depth1].get('Domain'))
			if DomainRecordInfos[depth1].get('Type') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Type', DomainRecordInfos[depth1].get('Type'))
			if DomainRecordInfos[depth1].get('Priority') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Priority', DomainRecordInfos[depth1].get('Priority'))
			if DomainRecordInfos[depth1].get('Value') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Value', DomainRecordInfos[depth1].get('Value'))
			if DomainRecordInfos[depth1].get('Ttl') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.Ttl', DomainRecordInfos[depth1].get('Ttl'))
			if DomainRecordInfos[depth1].get('NewRr') is not None:
				self.add_query_param('DomainRecordInfo.' + str(depth1 + 1) + '.NewRr', DomainRecordInfos[depth1].get('NewRr'))

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)