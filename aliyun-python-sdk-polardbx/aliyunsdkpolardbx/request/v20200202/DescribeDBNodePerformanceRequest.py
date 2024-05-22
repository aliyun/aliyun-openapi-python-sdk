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
from aliyunsdkpolardbx.endpoint import endpoint_data

class DescribeDBNodePerformanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'DescribeDBNodePerformance','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_DBNodeRole(self): # String
		return self.get_query_params().get('DBNodeRole')

	def set_DBNodeRole(self, DBNodeRole):  # String
		self.add_query_param('DBNodeRole', DBNodeRole)
	def get_CharacterType(self): # String
		return self.get_query_params().get('CharacterType')

	def set_CharacterType(self, CharacterType):  # String
		self.add_query_param('CharacterType', CharacterType)
	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_DBNodeIds(self): # String
		return self.get_query_params().get('DBNodeIds')

	def set_DBNodeIds(self, DBNodeIds):  # String
		self.add_query_param('DBNodeIds', DBNodeIds)
	def get_Key(self): # String
		return self.get_query_params().get('Key')

	def set_Key(self, Key):  # String
		self.add_query_param('Key', Key)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
