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
class UpdateSendMaterialNumRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'UpdateSendMaterialNum','trademark')

	def get_Num(self):
		return self.get_query_params().get('Num')

	def set_Num(self,Num):
		self.add_query_param('Num',Num)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_OperateType(self):
		return self.get_query_params().get('OperateType')

	def set_OperateType(self,OperateType):
		self.add_query_param('OperateType',OperateType)