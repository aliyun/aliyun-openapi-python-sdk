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
from aliyunsdknas.endpoint import endpoint_data

class ModifyAccessRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'ModifyAccessRule','nas')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RWAccessType(self):
		return self.get_query_params().get('RWAccessType')

	def set_RWAccessType(self,RWAccessType):
		self.add_query_param('RWAccessType',RWAccessType)

	def get_UserAccessType(self):
		return self.get_query_params().get('UserAccessType')

	def set_UserAccessType(self,UserAccessType):
		self.add_query_param('UserAccessType',UserAccessType)

	def get_FileSystemType(self):
		return self.get_query_params().get('FileSystemType')

	def set_FileSystemType(self,FileSystemType):
		self.add_query_param('FileSystemType',FileSystemType)

	def get_AccessRuleId(self):
		return self.get_query_params().get('AccessRuleId')

	def set_AccessRuleId(self,AccessRuleId):
		self.add_query_param('AccessRuleId',AccessRuleId)

	def get_SourceCidrIp(self):
		return self.get_query_params().get('SourceCidrIp')

	def set_SourceCidrIp(self,SourceCidrIp):
		self.add_query_param('SourceCidrIp',SourceCidrIp)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_AccessGroupName(self):
		return self.get_query_params().get('AccessGroupName')

	def set_AccessGroupName(self,AccessGroupName):
		self.add_query_param('AccessGroupName',AccessGroupName)