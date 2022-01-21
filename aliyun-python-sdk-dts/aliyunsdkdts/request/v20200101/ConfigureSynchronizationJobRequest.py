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

class ConfigureSynchronizationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ConfigureSynchronizationJob','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceEndpointInstanceId(self): # String
		return self.get_query_params().get('SourceEndpoint.InstanceId')

	def set_SourceEndpointInstanceId(self, SourceEndpointInstanceId):  # String
		self.add_query_param('SourceEndpoint.InstanceId', SourceEndpointInstanceId)
	def get_Checkpoint(self): # String
		return self.get_query_params().get('Checkpoint')

	def set_Checkpoint(self, Checkpoint):  # String
		self.add_query_param('Checkpoint', Checkpoint)
	def get_DestinationEndpointInstanceId(self): # String
		return self.get_query_params().get('DestinationEndpoint.InstanceId')

	def set_DestinationEndpointInstanceId(self, DestinationEndpointInstanceId):  # String
		self.add_query_param('DestinationEndpoint.InstanceId', DestinationEndpointInstanceId)
	def get_SourceEndpointIP(self): # String
		return self.get_query_params().get('SourceEndpoint.IP')

	def set_SourceEndpointIP(self, SourceEndpointIP):  # String
		self.add_query_param('SourceEndpoint.IP', SourceEndpointIP)
	def get_SynchronizationObjects(self): # String
		return self.get_body_params().get('SynchronizationObjects')

	def set_SynchronizationObjects(self, SynchronizationObjects):  # String
		self.add_body_params('SynchronizationObjects', SynchronizationObjects)
	def get_DestinationEndpointPassword(self): # String
		return self.get_query_params().get('DestinationEndpoint.Password')

	def set_DestinationEndpointPassword(self, DestinationEndpointPassword):  # String
		self.add_query_param('DestinationEndpoint.Password', DestinationEndpointPassword)
	def get_DataInitialization(self): # Boolean
		return self.get_query_params().get('DataInitialization')

	def set_DataInitialization(self, DataInitialization):  # Boolean
		self.add_query_param('DataInitialization', DataInitialization)
	def get_StructureInitialization(self): # Boolean
		return self.get_query_params().get('StructureInitialization')

	def set_StructureInitialization(self, StructureInitialization):  # Boolean
		self.add_query_param('StructureInitialization', StructureInitialization)
	def get_PartitionKeyModifyTime_Minute(self): # Boolean
		return self.get_query_params().get('PartitionKey.ModifyTime_Minute')

	def set_PartitionKeyModifyTime_Minute(self, PartitionKeyModifyTime_Minute):  # Boolean
		self.add_query_param('PartitionKey.ModifyTime_Minute', PartitionKeyModifyTime_Minute)
	def get_PartitionKeyModifyTime_Day(self): # Boolean
		return self.get_query_params().get('PartitionKey.ModifyTime_Day')

	def set_PartitionKeyModifyTime_Day(self, PartitionKeyModifyTime_Day):  # Boolean
		self.add_query_param('PartitionKey.ModifyTime_Day', PartitionKeyModifyTime_Day)
	def get_SourceEndpointInstanceType(self): # String
		return self.get_query_params().get('SourceEndpoint.InstanceType')

	def set_SourceEndpointInstanceType(self, SourceEndpointInstanceType):  # String
		self.add_query_param('SourceEndpoint.InstanceType', SourceEndpointInstanceType)
	def get_SynchronizationJobId(self): # String
		return self.get_query_params().get('SynchronizationJobId')

	def set_SynchronizationJobId(self, SynchronizationJobId):  # String
		self.add_query_param('SynchronizationJobId', SynchronizationJobId)
	def get_SynchronizationJobName(self): # String
		return self.get_query_params().get('SynchronizationJobName')

	def set_SynchronizationJobName(self, SynchronizationJobName):  # String
		self.add_query_param('SynchronizationJobName', SynchronizationJobName)
	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_SourceEndpointUserName(self): # String
		return self.get_query_params().get('SourceEndpoint.UserName')

	def set_SourceEndpointUserName(self, SourceEndpointUserName):  # String
		self.add_query_param('SourceEndpoint.UserName', SourceEndpointUserName)
	def get_SourceEndpointDatabaseName(self): # String
		return self.get_query_params().get('SourceEndpoint.DatabaseName')

	def set_SourceEndpointDatabaseName(self, SourceEndpointDatabaseName):  # String
		self.add_query_param('SourceEndpoint.DatabaseName', SourceEndpointDatabaseName)
	def get_PartitionKeyModifyTime_Month(self): # Boolean
		return self.get_query_params().get('PartitionKey.ModifyTime_Month')

	def set_PartitionKeyModifyTime_Month(self, PartitionKeyModifyTime_Month):  # Boolean
		self.add_query_param('PartitionKey.ModifyTime_Month', PartitionKeyModifyTime_Month)
	def get_SourceEndpointPort(self): # String
		return self.get_query_params().get('SourceEndpoint.Port')

	def set_SourceEndpointPort(self, SourceEndpointPort):  # String
		self.add_query_param('SourceEndpoint.Port', SourceEndpointPort)
	def get_SourceEndpointOwnerID(self): # String
		return self.get_query_params().get('SourceEndpoint.OwnerID')

	def set_SourceEndpointOwnerID(self, SourceEndpointOwnerID):  # String
		self.add_query_param('SourceEndpoint.OwnerID', SourceEndpointOwnerID)
	def get_DestinationEndpointUserName(self): # String
		return self.get_query_params().get('DestinationEndpoint.UserName')

	def set_DestinationEndpointUserName(self, DestinationEndpointUserName):  # String
		self.add_query_param('DestinationEndpoint.UserName', DestinationEndpointUserName)
	def get_DestinationEndpointPort(self): # String
		return self.get_query_params().get('DestinationEndpoint.Port')

	def set_DestinationEndpointPort(self, DestinationEndpointPort):  # String
		self.add_query_param('DestinationEndpoint.Port', DestinationEndpointPort)
	def get_PartitionKeyModifyTime_Year(self): # Boolean
		return self.get_query_params().get('PartitionKey.ModifyTime_Year')

	def set_PartitionKeyModifyTime_Year(self, PartitionKeyModifyTime_Year):  # Boolean
		self.add_query_param('PartitionKey.ModifyTime_Year', PartitionKeyModifyTime_Year)
	def get_SourceEndpointRole(self): # String
		return self.get_query_params().get('SourceEndpoint.Role')

	def set_SourceEndpointRole(self, SourceEndpointRole):  # String
		self.add_query_param('SourceEndpoint.Role', SourceEndpointRole)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_PartitionKeyModifyTime_Hour(self): # Boolean
		return self.get_query_params().get('PartitionKey.ModifyTime_Hour')

	def set_PartitionKeyModifyTime_Hour(self, PartitionKeyModifyTime_Hour):  # Boolean
		self.add_query_param('PartitionKey.ModifyTime_Hour', PartitionKeyModifyTime_Hour)
	def get_DestinationEndpointDataBaseName(self): # String
		return self.get_query_params().get('DestinationEndpoint.DataBaseName')

	def set_DestinationEndpointDataBaseName(self, DestinationEndpointDataBaseName):  # String
		self.add_query_param('DestinationEndpoint.DataBaseName', DestinationEndpointDataBaseName)
	def get_SourceEndpointPassword(self): # String
		return self.get_query_params().get('SourceEndpoint.Password')

	def set_SourceEndpointPassword(self, SourceEndpointPassword):  # String
		self.add_query_param('SourceEndpoint.Password', SourceEndpointPassword)
	def get_MigrationReserved(self): # String
		return self.get_query_params().get('MigrationReserved')

	def set_MigrationReserved(self, MigrationReserved):  # String
		self.add_query_param('MigrationReserved', MigrationReserved)
	def get_DestinationEndpointIP(self): # String
		return self.get_query_params().get('DestinationEndpoint.IP')

	def set_DestinationEndpointIP(self, DestinationEndpointIP):  # String
		self.add_query_param('DestinationEndpoint.IP', DestinationEndpointIP)
	def get_DestinationEndpointInstanceType(self): # String
		return self.get_query_params().get('DestinationEndpoint.InstanceType')

	def set_DestinationEndpointInstanceType(self, DestinationEndpointInstanceType):  # String
		self.add_query_param('DestinationEndpoint.InstanceType', DestinationEndpointInstanceType)
	def get_SynchronizationDirection(self): # String
		return self.get_query_params().get('SynchronizationDirection')

	def set_SynchronizationDirection(self, SynchronizationDirection):  # String
		self.add_query_param('SynchronizationDirection', SynchronizationDirection)
