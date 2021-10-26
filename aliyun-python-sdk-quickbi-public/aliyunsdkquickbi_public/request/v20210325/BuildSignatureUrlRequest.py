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
from aliyunsdkquickbi_public.endpoint import endpoint_data

class BuildSignatureUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2021-03-25', 'BuildSignatureUrl','quickbi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Watermark(self):
		return self.get_query_params().get('Watermark')

	def set_Watermark(self,Watermark):
		self.add_query_param('Watermark',Watermark)

	def get_AccountType(self):
		return self.get_query_params().get('AccountType')

	def set_AccountType(self,AccountType):
		self.add_query_param('AccountType',AccountType)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_WorksId(self):
		return self.get_query_params().get('WorksId')

	def set_WorksId(self,WorksId):
		self.add_query_param('WorksId',WorksId)

	def get_WithHost(self):
		return self.get_query_params().get('WithHost')

	def set_WithHost(self,WithHost):
		self.add_query_param('WithHost',WithHost)

	def get_ExpireMin(self):
		return self.get_query_params().get('ExpireMin')

	def set_ExpireMin(self,ExpireMin):
		self.add_query_param('ExpireMin',ExpireMin)