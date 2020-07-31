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
from aliyunsdkalinlp.endpoint import endpoint_data

class GetWsCustomizedChEntertainmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alinlp', '2020-06-29', 'GetWsCustomizedChEntertainment','alinlp')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ServiceCode(self):
		return self.get_body_params().get('ServiceCode')

	def set_ServiceCode(self,ServiceCode):
		self.add_body_params('ServiceCode', ServiceCode)

	def get_TokenizerId(self):
		return self.get_body_params().get('TokenizerId')

	def set_TokenizerId(self,TokenizerId):
		self.add_body_params('TokenizerId', TokenizerId)

	def get_Text(self):
		return self.get_body_params().get('Text')

	def set_Text(self,Text):
		self.add_body_params('Text', Text)

	def get_OutType(self):
		return self.get_body_params().get('OutType')

	def set_OutType(self,OutType):
		self.add_body_params('OutType', OutType)