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
from aliyunsdkdts.endpoint import endpoint_data

class ConfigureSubscriptionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ConfigureSubscription','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceEndpointRegion(self): # String
		return self.get_query_params().get('SourceEndpointRegion')

	def set_SourceEndpointRegion(self, SourceEndpointRegion):  # String
		self.add_query_param('SourceEndpointRegion', SourceEndpointRegion)
	def get_Checkpoint(self): # String
		return self.get_query_params().get('Checkpoint')

	def set_Checkpoint(self, Checkpoint):  # String
		self.add_query_param('Checkpoint', Checkpoint)
	def get_SubscriptionInstanceVSwitchId(self): # String
		return self.get_query_params().get('SubscriptionInstanceVSwitchId')

	def set_SubscriptionInstanceVSwitchId(self, SubscriptionInstanceVSwitchId):  # String
		self.add_query_param('SubscriptionInstanceVSwitchId', SubscriptionInstanceVSwitchId)
	def get_DelayNotice(self): # Boolean
		return self.get_query_params().get('DelayNotice')

	def set_DelayNotice(self, DelayNotice):  # Boolean
		self.add_query_param('DelayNotice', DelayNotice)
	def get_SourceEndpointInstanceID(self): # String
		return self.get_query_params().get('SourceEndpointInstanceID')

	def set_SourceEndpointInstanceID(self, SourceEndpointInstanceID):  # String
		self.add_query_param('SourceEndpointInstanceID', SourceEndpointInstanceID)
	def get_SourceEndpointUserName(self): # String
		return self.get_query_params().get('SourceEndpointUserName')

	def set_SourceEndpointUserName(self, SourceEndpointUserName):  # String
		self.add_query_param('SourceEndpointUserName', SourceEndpointUserName)
	def get_SourceEndpointOwnerID(self): # String
		return self.get_query_params().get('SourceEndpointOwnerID')

	def set_SourceEndpointOwnerID(self, SourceEndpointOwnerID):  # String
		self.add_query_param('SourceEndpointOwnerID', SourceEndpointOwnerID)
	def get_DedicatedClusterId(self): # String
		return self.get_query_params().get('DedicatedClusterId')

	def set_DedicatedClusterId(self, DedicatedClusterId):  # String
		self.add_query_param('DedicatedClusterId', DedicatedClusterId)
	def get_DelayPhone(self): # String
		return self.get_query_params().get('DelayPhone')

	def set_DelayPhone(self, DelayPhone):  # String
		self.add_query_param('DelayPhone', DelayPhone)
	def get_SubscriptionDataTypeDML(self): # Boolean
		return self.get_query_params().get('SubscriptionDataTypeDML')

	def set_SubscriptionDataTypeDML(self, SubscriptionDataTypeDML):  # Boolean
		self.add_query_param('SubscriptionDataTypeDML', SubscriptionDataTypeDML)
	def get_SourceEndpointDatabaseName(self): # String
		return self.get_query_params().get('SourceEndpointDatabaseName')

	def set_SourceEndpointDatabaseName(self, SourceEndpointDatabaseName):  # String
		self.add_query_param('SourceEndpointDatabaseName', SourceEndpointDatabaseName)
	def get_SourceEndpointIP(self): # String
		return self.get_query_params().get('SourceEndpointIP')

	def set_SourceEndpointIP(self, SourceEndpointIP):  # String
		self.add_query_param('SourceEndpointIP', SourceEndpointIP)
	def get_ErrorPhone(self): # String
		return self.get_query_params().get('ErrorPhone')

	def set_ErrorPhone(self, ErrorPhone):  # String
		self.add_query_param('ErrorPhone', ErrorPhone)
	def get_Reserve(self): # String
		return self.get_query_params().get('Reserve')

	def set_Reserve(self, Reserve):  # String
		self.add_query_param('Reserve', Reserve)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
	def get_DbList(self): # String
		return self.get_query_params().get('DbList')

	def set_DbList(self, DbList):  # String
		self.add_query_param('DbList', DbList)
	def get_SubscriptionInstanceNetworkType(self): # String
		return self.get_query_params().get('SubscriptionInstanceNetworkType')

	def set_SubscriptionInstanceNetworkType(self, SubscriptionInstanceNetworkType):  # String
		self.add_query_param('SubscriptionInstanceNetworkType', SubscriptionInstanceNetworkType)
	def get_SubscriptionDataTypeDDL(self): # Boolean
		return self.get_query_params().get('SubscriptionDataTypeDDL')

	def set_SubscriptionDataTypeDDL(self, SubscriptionDataTypeDDL):  # Boolean
		self.add_query_param('SubscriptionDataTypeDDL', SubscriptionDataTypeDDL)
	def get_SourceEndpointPassword(self): # String
		return self.get_query_params().get('SourceEndpointPassword')

	def set_SourceEndpointPassword(self, SourceEndpointPassword):  # String
		self.add_query_param('SourceEndpointPassword', SourceEndpointPassword)
	def get_SourceEndpointPort(self): # String
		return self.get_query_params().get('SourceEndpointPort')

	def set_SourceEndpointPort(self, SourceEndpointPort):  # String
		self.add_query_param('SourceEndpointPort', SourceEndpointPort)
	def get_SubscriptionInstanceVPCId(self): # String
		return self.get_query_params().get('SubscriptionInstanceVPCId')

	def set_SubscriptionInstanceVPCId(self, SubscriptionInstanceVPCId):  # String
		self.add_query_param('SubscriptionInstanceVPCId', SubscriptionInstanceVPCId)
	def get_DelayRuleTime(self): # Long
		return self.get_query_params().get('DelayRuleTime')

	def set_DelayRuleTime(self, DelayRuleTime):  # Long
		self.add_query_param('DelayRuleTime', DelayRuleTime)
	def get_SourceEndpointInstanceType(self): # String
		return self.get_query_params().get('SourceEndpointInstanceType')

	def set_SourceEndpointInstanceType(self, SourceEndpointInstanceType):  # String
		self.add_query_param('SourceEndpointInstanceType', SourceEndpointInstanceType)
	def get_DtsJobName(self): # String
		return self.get_query_params().get('DtsJobName')

	def set_DtsJobName(self, DtsJobName):  # String
		self.add_query_param('DtsJobName', DtsJobName)
	def get_SourceEndpointOracleSID(self): # String
		return self.get_query_params().get('SourceEndpointOracleSID')

	def set_SourceEndpointOracleSID(self, SourceEndpointOracleSID):  # String
		self.add_query_param('SourceEndpointOracleSID', SourceEndpointOracleSID)
	def get_ErrorNotice(self): # Boolean
		return self.get_query_params().get('ErrorNotice')

	def set_ErrorNotice(self, ErrorNotice):  # Boolean
		self.add_query_param('ErrorNotice', ErrorNotice)
	def get_SourceEndpointRole(self): # String
		return self.get_query_params().get('SourceEndpointRole')

	def set_SourceEndpointRole(self, SourceEndpointRole):  # String
		self.add_query_param('SourceEndpointRole', SourceEndpointRole)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
	def get_SourceEndpointEngineName(self): # String
		return self.get_query_params().get('SourceEndpointEngineName')

	def set_SourceEndpointEngineName(self, SourceEndpointEngineName):  # String
		self.add_query_param('SourceEndpointEngineName', SourceEndpointEngineName)
