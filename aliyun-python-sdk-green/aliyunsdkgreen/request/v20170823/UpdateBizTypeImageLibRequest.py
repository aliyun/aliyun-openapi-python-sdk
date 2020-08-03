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

class UpdateBizTypeImageLibRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateBizTypeImageLib','green')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)

	def get_White(self):
		return self.get_query_params().get('White')

	def set_White(self,White):
		self.add_query_param('White',White)

	def get_Review(self):
		return self.get_query_params().get('Review')

	def set_Review(self,Review):
		self.add_query_param('Review',Review)

	def get_BizTypeName(self):
		return self.get_query_params().get('BizTypeName')

	def set_BizTypeName(self,BizTypeName):
		self.add_query_param('BizTypeName',BizTypeName)

	def get_Black(self):
		return self.get_query_params().get('Black')

	def set_Black(self,Black):
		self.add_query_param('Black',Black)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)