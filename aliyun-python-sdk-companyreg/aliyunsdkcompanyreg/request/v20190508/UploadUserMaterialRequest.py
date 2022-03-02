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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class UploadUserMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'UploadUserMaterial')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_Attributes(self): # RepeatList
		return self.get_query_params().get('Attribute')

	def set_Attributes(self, Attribute):  # RepeatList
		for depth1 in range(len(Attribute)):
			if Attribute[depth1].get('Value') is not None:
				self.add_query_param('Attribute.' + str(depth1 + 1) + '.Value', Attribute[depth1].get('Value'))
			if Attribute[depth1].get('Key') is not None:
				self.add_query_param('Attribute.' + str(depth1 + 1) + '.Key', Attribute[depth1].get('Key'))
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
