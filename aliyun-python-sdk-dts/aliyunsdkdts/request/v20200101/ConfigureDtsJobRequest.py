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

class ConfigureDtsJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ConfigureDtsJob','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Checkpoint(self): # String
		return self.get_query_params().get('Checkpoint')

	def set_Checkpoint(self, Checkpoint):  # String
		self.add_query_param('Checkpoint', Checkpoint)
	def get_SourceEndpointUserName(self): # String
		return self.get_query_params().get('SourceEndpointUserName')

	def set_SourceEndpointUserName(self, SourceEndpointUserName):  # String
		self.add_query_param('SourceEndpointUserName', SourceEndpointUserName)
	def get_DelayPhone(self): # String
		return self.get_query_params().get('DelayPhone')

	def set_DelayPhone(self, DelayPhone):  # String
		self.add_query_param('DelayPhone', DelayPhone)
	def get_SourceEndpointIP(self): # String
		return self.get_query_params().get('SourceEndpointIP')

	def set_SourceEndpointIP(self, SourceEndpointIP):  # String
		self.add_query_param('SourceEndpointIP', SourceEndpointIP)
	def get_ErrorPhone(self): # String
		return self.get_query_params().get('ErrorPhone')

	def set_ErrorPhone(self, ErrorPhone):  # String
		self.add_query_param('ErrorPhone', ErrorPhone)
	def get_DestinationEndpointUserName(self): # String
		return self.get_query_params().get('DestinationEndpointUserName')

	def set_DestinationEndpointUserName(self, DestinationEndpointUserName):  # String
		self.add_query_param('DestinationEndpointUserName', DestinationEndpointUserName)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
	def get_DbList(self): # String
		return self.get_body_params().get('DbList')

	def set_DbList(self, DbList):  # String
		self.add_body_params('DbList', DbList)
	def get_DestinationEndpointOracleSID(self): # String
		return self.get_query_params().get('DestinationEndpointOracleSID')

	def set_DestinationEndpointOracleSID(self, DestinationEndpointOracleSID):  # String
		self.add_query_param('DestinationEndpointOracleSID', DestinationEndpointOracleSID)
	def get_DestinationEndpointPort(self): # String
		return self.get_query_params().get('DestinationEndpointPort')

	def set_DestinationEndpointPort(self, DestinationEndpointPort):  # String
		self.add_query_param('DestinationEndpointPort', DestinationEndpointPort)
	def get_SourceEndpointPassword(self): # String
		return self.get_query_params().get('SourceEndpointPassword')

	def set_SourceEndpointPassword(self, SourceEndpointPassword):  # String
		self.add_query_param('SourceEndpointPassword', SourceEndpointPassword)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_JobType(self): # String
		return self.get_query_params().get('JobType')

	def set_JobType(self, JobType):  # String
		self.add_query_param('JobType', JobType)
	def get_DelayRuleTime(self): # Long
		return self.get_query_params().get('DelayRuleTime')

	def set_DelayRuleTime(self, DelayRuleTime):  # Long
		self.add_query_param('DelayRuleTime', DelayRuleTime)
	def get_DestinationEndpointIP(self): # String
		return self.get_query_params().get('DestinationEndpointIP')

	def set_DestinationEndpointIP(self, DestinationEndpointIP):  # String
		self.add_query_param('DestinationEndpointIP', DestinationEndpointIP)
	def get_SourceEndpointInstanceType(self): # String
		return self.get_query_params().get('SourceEndpointInstanceType')

	def set_SourceEndpointInstanceType(self, SourceEndpointInstanceType):  # String
		self.add_query_param('SourceEndpointInstanceType', SourceEndpointInstanceType)
	def get_DtsJobName(self): # String
		return self.get_query_params().get('DtsJobName')

	def set_DtsJobName(self, DtsJobName):  # String
		self.add_query_param('DtsJobName', DtsJobName)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
	def get_SynchronizationDirection(self): # String
		return self.get_query_params().get('SynchronizationDirection')

	def set_SynchronizationDirection(self, SynchronizationDirection):  # String
		self.add_query_param('SynchronizationDirection', SynchronizationDirection)
	def get_SourceEndpointRegion(self): # String
		return self.get_query_params().get('SourceEndpointRegion')

	def set_SourceEndpointRegion(self, SourceEndpointRegion):  # String
		self.add_query_param('SourceEndpointRegion', SourceEndpointRegion)
	def get_DelayNotice(self): # Boolean
		return self.get_query_params().get('DelayNotice')

	def set_DelayNotice(self, DelayNotice):  # Boolean
		self.add_query_param('DelayNotice', DelayNotice)
	def get_DestinationEndpointInstanceType(self): # String
		return self.get_query_params().get('DestinationEndpointInstanceType')

	def set_DestinationEndpointInstanceType(self, DestinationEndpointInstanceType):  # String
		self.add_query_param('DestinationEndpointInstanceType', DestinationEndpointInstanceType)
	def get_DataInitialization(self): # Boolean
		return self.get_query_params().get('DataInitialization')

	def set_DataInitialization(self, DataInitialization):  # Boolean
		self.add_query_param('DataInitialization', DataInitialization)
	def get_SourceEndpointInstanceID(self): # String
		return self.get_query_params().get('SourceEndpointInstanceID')

	def set_SourceEndpointInstanceID(self, SourceEndpointInstanceID):  # String
		self.add_query_param('SourceEndpointInstanceID', SourceEndpointInstanceID)
	def get_StructureInitialization(self): # Boolean
		return self.get_query_params().get('StructureInitialization')

	def set_StructureInitialization(self, StructureInitialization):  # Boolean
		self.add_query_param('StructureInitialization', StructureInitialization)
	def get_SourceEndpointOwnerID(self): # String
		return self.get_query_params().get('SourceEndpointOwnerID')

	def set_SourceEndpointOwnerID(self, SourceEndpointOwnerID):  # String
		self.add_query_param('SourceEndpointOwnerID', SourceEndpointOwnerID)
	def get_DedicatedClusterId(self): # String
		return self.get_query_params().get('DedicatedClusterId')

	def set_DedicatedClusterId(self, DedicatedClusterId):  # String
		self.add_query_param('DedicatedClusterId', DedicatedClusterId)
	def get_SourceEndpointDatabaseName(self): # String
		return self.get_query_params().get('SourceEndpointDatabaseName')

	def set_SourceEndpointDatabaseName(self, SourceEndpointDatabaseName):  # String
		self.add_query_param('SourceEndpointDatabaseName', SourceEndpointDatabaseName)
	def get_DestinationEndpointRegion(self): # String
		return self.get_query_params().get('DestinationEndpointRegion')

	def set_DestinationEndpointRegion(self, DestinationEndpointRegion):  # String
		self.add_query_param('DestinationEndpointRegion', DestinationEndpointRegion)
	def get_Reserve(self): # String
		return self.get_body_params().get('Reserve')

	def set_Reserve(self, Reserve):  # String
		self.add_body_params('Reserve', Reserve)
	def get_DataSynchronization(self): # Boolean
		return self.get_query_params().get('DataSynchronization')

	def set_DataSynchronization(self, DataSynchronization):  # Boolean
		self.add_query_param('DataSynchronization', DataSynchronization)
	def get_DestinationEndpointEngineName(self): # String
		return self.get_query_params().get('DestinationEndpointEngineName')

	def set_DestinationEndpointEngineName(self, DestinationEndpointEngineName):  # String
		self.add_query_param('DestinationEndpointEngineName', DestinationEndpointEngineName)
	def get_DestinationEndpointInstanceID(self): # String
		return self.get_query_params().get('DestinationEndpointInstanceID')

	def set_DestinationEndpointInstanceID(self, DestinationEndpointInstanceID):  # String
		self.add_query_param('DestinationEndpointInstanceID', DestinationEndpointInstanceID)
	def get_SourceEndpointPort(self): # String
		return self.get_query_params().get('SourceEndpointPort')

	def set_SourceEndpointPort(self, SourceEndpointPort):  # String
		self.add_query_param('SourceEndpointPort', SourceEndpointPort)
	def get_SourceEndpointOracleSID(self): # String
		return self.get_query_params().get('SourceEndpointOracleSID')

	def set_SourceEndpointOracleSID(self, SourceEndpointOracleSID):  # String
		self.add_query_param('SourceEndpointOracleSID', SourceEndpointOracleSID)
	def get_DestinationEndpointDataBaseName(self): # String
		return self.get_query_params().get('DestinationEndpointDataBaseName')

	def set_DestinationEndpointDataBaseName(self, DestinationEndpointDataBaseName):  # String
		self.add_query_param('DestinationEndpointDataBaseName', DestinationEndpointDataBaseName)
	def get_ErrorNotice(self): # Boolean
		return self.get_query_params().get('ErrorNotice')

	def set_ErrorNotice(self, ErrorNotice):  # Boolean
		self.add_query_param('ErrorNotice', ErrorNotice)
	def get_SourceEndpointRole(self): # String
		return self.get_query_params().get('SourceEndpointRole')

	def set_SourceEndpointRole(self, SourceEndpointRole):  # String
		self.add_query_param('SourceEndpointRole', SourceEndpointRole)
	def get_DestinationEndpointPassword(self): # String
		return self.get_query_params().get('DestinationEndpointPassword')

	def set_DestinationEndpointPassword(self, DestinationEndpointPassword):  # String
		self.add_query_param('DestinationEndpointPassword', DestinationEndpointPassword)
	def get_SourceEndpointEngineName(self): # String
		return self.get_query_params().get('SourceEndpointEngineName')

	def set_SourceEndpointEngineName(self, SourceEndpointEngineName):  # String
		self.add_query_param('SourceEndpointEngineName', SourceEndpointEngineName)
