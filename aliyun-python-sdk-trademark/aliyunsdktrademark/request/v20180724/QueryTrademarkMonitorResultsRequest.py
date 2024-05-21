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
class QueryTrademarkMonitorResultsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'QueryTrademarkMonitorResults','trademark')

	def get_ActionType(self):
		return self.get_query_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_query_param('ActionType',ActionType)

	def get_TmName(self):
		return self.get_query_params().get('TmName')

	def set_TmName(self,TmName):
		self.add_query_param('TmName',TmName)

	def get_ApplyYear(self):
		return self.get_query_params().get('ApplyYear')

	def set_ApplyYear(self,ApplyYear):
		self.add_query_param('ApplyYear',ApplyYear)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ProcedureStatus(self):
		return self.get_query_params().get('ProcedureStatus')

	def set_ProcedureStatus(self,ProcedureStatus):
		self.add_query_param('ProcedureStatus',ProcedureStatus)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)

	def get_Classification(self):
		return self.get_query_params().get('Classification')

	def set_Classification(self,Classification):
		self.add_query_param('Classification',Classification)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_RegistrationNumber(self):
		return self.get_query_params().get('RegistrationNumber')

	def set_RegistrationNumber(self,RegistrationNumber):
		self.add_query_param('RegistrationNumber',RegistrationNumber)