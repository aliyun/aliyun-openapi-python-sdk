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
from aliyunsdkecd.endpoint import endpoint_data

class VerifyCenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'VerifyCen')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_CenOwnerId(self): # Long
		return self.get_query_params().get('CenOwnerId')

	def set_CenOwnerId(self, CenOwnerId):  # Long
		self.add_query_param('CenOwnerId', CenOwnerId)
	def get_VerifyCode(self): # String
		return self.get_query_params().get('VerifyCode')

	def set_VerifyCode(self, VerifyCode):  # String
		self.add_query_param('VerifyCode', VerifyCode)
	def get_CidrBlock(self): # String
		return self.get_query_params().get('CidrBlock')

	def set_CidrBlock(self, CidrBlock):  # String
		self.add_query_param('CidrBlock', CidrBlock)
