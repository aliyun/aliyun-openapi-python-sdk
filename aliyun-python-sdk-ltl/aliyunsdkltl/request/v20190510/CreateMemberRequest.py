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
from aliyunsdkltl.endpoint import endpoint_data

class CreateMemberRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ltl', '2019-05-10', 'CreateMember')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ApiVersion(self): # String
		return self.get_query_params().get('ApiVersion')

	def set_ApiVersion(self, ApiVersion):  # String
		self.add_query_param('ApiVersion', ApiVersion)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_BizChainId(self): # String
		return self.get_query_params().get('BizChainId')

	def set_BizChainId(self, BizChainId):  # String
		self.add_query_param('BizChainId', BizChainId)
	def get_MemberUid(self): # String
		return self.get_query_params().get('MemberUid')

	def set_MemberUid(self, MemberUid):  # String
		self.add_query_param('MemberUid', MemberUid)
	def get_MemberContact(self): # String
		return self.get_query_params().get('MemberContact')

	def set_MemberContact(self, MemberContact):  # String
		self.add_query_param('MemberContact', MemberContact)
	def get_MemberPhone(self): # String
		return self.get_query_params().get('MemberPhone')

	def set_MemberPhone(self, MemberPhone):  # String
		self.add_query_param('MemberPhone', MemberPhone)
	def get_MemberName(self): # String
		return self.get_query_params().get('MemberName')

	def set_MemberName(self, MemberName):  # String
		self.add_query_param('MemberName', MemberName)
