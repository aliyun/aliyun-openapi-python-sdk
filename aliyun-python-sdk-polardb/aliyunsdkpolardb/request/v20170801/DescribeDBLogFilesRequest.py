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
from aliyunsdkpolardb.endpoint import endpoint_data

class DescribeDBLogFilesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'DescribeDBLogFiles','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBNodeId(self): # String
		return self.get_query_params().get('DBNodeId')

	def set_DBNodeId(self, DBNodeId):  # String
		self.add_query_param('DBNodeId', DBNodeId)
	def get_SimulateListId(self): # String
		return self.get_query_params().get('SimulateListId')

	def set_SimulateListId(self, SimulateListId):  # String
		self.add_query_param('SimulateListId', SimulateListId)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_LogType(self): # String
		return self.get_query_params().get('LogType')

	def set_LogType(self, LogType):  # String
		self.add_query_param('LogType', LogType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DescribeSimulateSwitchMode(self): # String
		return self.get_query_params().get('DescribeSimulateSwitchMode')

	def set_DescribeSimulateSwitchMode(self, DescribeSimulateSwitchMode):  # String
		self.add_query_param('DescribeSimulateSwitchMode', DescribeSimulateSwitchMode)
	def get_SimulateStatusList(self): # String
		return self.get_query_params().get('SimulateStatusList')

	def set_SimulateStatusList(self, SimulateStatusList):  # String
		self.add_query_param('SimulateStatusList', SimulateStatusList)
	def get_SimulateModeList(self): # String
		return self.get_query_params().get('SimulateModeList')

	def set_SimulateModeList(self, SimulateModeList):  # String
		self.add_query_param('SimulateModeList', SimulateModeList)
