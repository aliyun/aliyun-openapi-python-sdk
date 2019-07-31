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
class DescribeBackupSourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeBackupSources','hbr')

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_Filterss(self):
		return self.get_query_params().get('Filterss')

	def set_Filterss(self,Filterss):
		for i in range(len(Filterss)):	
			for j in range(len(Filterss[i].get('Valuess'))):
				if Filterss[i].get('Valuess')[j] is not None:
					self.add_query_param('Filters.' + str(i + 1) + '.Values.'+str(j + 1), Filterss[i].get('Valuess')[j])
			if Filterss[i].get('Key') is not None:
				self.add_query_param('Filters.' + str(i + 1) + '.Key' , Filterss[i].get('Key'))


	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)