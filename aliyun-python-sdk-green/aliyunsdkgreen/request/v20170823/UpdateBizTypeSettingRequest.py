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
from aliyunsdkgreen.endpoint import endpoint_data

class UpdateBizTypeSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateBizTypeSetting','green')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Antispam(self):
		return self.get_query_params().get('Antispam')

	def set_Antispam(self,Antispam):
		self.add_query_param('Antispam',Antispam)

	def get_Porn(self):
		return self.get_query_params().get('Porn')

	def set_Porn(self,Porn):
		self.add_query_param('Porn',Porn)

	def get_Terrorism(self):
		return self.get_query_params().get('Terrorism')

	def set_Terrorism(self,Terrorism):
		self.add_query_param('Terrorism',Terrorism)

	def get_BizTypeName(self):
		return self.get_query_params().get('BizTypeName')

	def set_BizTypeName(self,BizTypeName):
		self.add_query_param('BizTypeName',BizTypeName)

	def get_Ad(self):
		return self.get_query_params().get('Ad')

	def set_Ad(self,Ad):
		self.add_query_param('Ad',Ad)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)