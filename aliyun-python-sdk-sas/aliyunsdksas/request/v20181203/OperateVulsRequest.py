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
from aliyunsdksas.endpoint import endpoint_data

class OperateVulsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'OperateVuls','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Reason(self):
		return self.get_query_params().get('Reason')

	def set_Reason(self,Reason):
		self.add_query_param('Reason',Reason)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_VulNamess(self):
		return self.get_query_params().get('VulNames')

	def set_VulNamess(self, VulNamess):
		for depth1 in range(len(VulNamess)):
			if VulNamess[depth1] is not None:
				self.add_query_param('VulNames.' + str(depth1 + 1) , VulNamess[depth1])

	def get_Precondition(self):
		return self.get_query_params().get('Precondition')

	def set_Precondition(self,Precondition):
		self.add_query_param('Precondition',Precondition)

	def get_OperateType(self):
		return self.get_query_params().get('OperateType')

	def set_OperateType(self,OperateType):
		self.add_query_param('OperateType',OperateType)

	def get_Uuidss(self):
		return self.get_query_params().get('Uuids')

	def set_Uuidss(self, Uuidss):
		for depth1 in range(len(Uuidss)):
			if Uuidss[depth1] is not None:
				self.add_query_param('Uuids.' + str(depth1 + 1) , Uuidss[depth1])