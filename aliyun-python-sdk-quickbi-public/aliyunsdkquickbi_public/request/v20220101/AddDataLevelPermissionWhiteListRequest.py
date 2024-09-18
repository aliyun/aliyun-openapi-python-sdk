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

class AddDataLevelPermissionWhiteListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'AddDataLevelPermissionWhiteList','2.2.0')
		self.set_method('POST')

	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_CubeId(self): # String
		return self.get_query_params().get('CubeId')

	def set_CubeId(self, CubeId):  # String
		self.add_query_param('CubeId', CubeId)
	def get_TargetIds(self): # String
		return self.get_query_params().get('TargetIds')

	def set_TargetIds(self, TargetIds):  # String
		self.add_query_param('TargetIds', TargetIds)
	def get_RuleType(self): # String
		return self.get_query_params().get('RuleType')

	def set_RuleType(self, RuleType):  # String
		self.add_query_param('RuleType', RuleType)
	def get_OperateType(self): # String
		return self.get_query_params().get('OperateType')

	def set_OperateType(self, OperateType):  # String
		self.add_query_param('OperateType', OperateType)
