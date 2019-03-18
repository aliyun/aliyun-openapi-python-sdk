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
class ProceedTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ccs', '2017-10-01', 'ProceedTicket','ccs')

	def get_Memo(self):
		return self.get_query_params().get('Memo')

	def set_Memo(self,Memo):
		self.add_query_param('Memo',Memo)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_CcsInstanceId(self):
		return self.get_query_params().get('CcsInstanceId')

	def set_CcsInstanceId(self,CcsInstanceId):
		self.add_query_param('CcsInstanceId',CcsInstanceId)

	def get_Operation(self):
		return self.get_query_params().get('Operation')

	def set_Operation(self,Operation):
		self.add_query_param('Operation',Operation)

	def get_OperatorId(self):
		return self.get_query_params().get('OperatorId')

	def set_OperatorId(self,OperatorId):
		self.add_query_param('OperatorId',OperatorId)