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
class ProcessCompanyRegOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'ProcessCompanyRegOrder','companyreg')

	def get_ActionType(self):
		return self.get_query_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_query_param('ActionType',ActionType)

	def get_BizCode(self):
		return self.get_query_params().get('BizCode')

	def set_BizCode(self,BizCode):
		self.add_query_param('BizCode',BizCode)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_ActionRequestId(self):
		return self.get_query_params().get('ActionRequestId')

	def set_ActionRequestId(self,ActionRequestId):
		self.add_query_param('ActionRequestId',ActionRequestId)

	def get_OperatorType(self):
		return self.get_query_params().get('OperatorType')

	def set_OperatorType(self,OperatorType):
		self.add_query_param('OperatorType',OperatorType)

	def get_ActionInfo(self):
		return self.get_query_params().get('ActionInfo')

	def set_ActionInfo(self,ActionInfo):
		self.add_query_param('ActionInfo',ActionInfo)