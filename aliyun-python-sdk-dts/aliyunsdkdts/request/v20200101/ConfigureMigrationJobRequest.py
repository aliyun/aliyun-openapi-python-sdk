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

class ConfigureMigrationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ConfigureMigrationJob','dts')

	def get_SourceEndpointInstanceID(self):
		return self.get_query_params().get('SourceEndpoint.InstanceID')

	def set_SourceEndpointInstanceID(self,SourceEndpointInstanceID):
		self.add_query_param('SourceEndpoint.InstanceID',SourceEndpointInstanceID)

	def get_Checkpoint(self):
		return self.get_query_params().get('Checkpoint')

	def set_Checkpoint(self,Checkpoint):
		self.add_query_param('Checkpoint',Checkpoint)

	def get_SourceEndpointEngineName(self):
		return self.get_query_params().get('SourceEndpoint.EngineName')

	def set_SourceEndpointEngineName(self,SourceEndpointEngineName):
		self.add_query_param('SourceEndpoint.EngineName',SourceEndpointEngineName)

	def get_SourceEndpointOracleSID(self):
		return self.get_query_params().get('SourceEndpoint.OracleSID')

	def set_SourceEndpointOracleSID(self,SourceEndpointOracleSID):
		self.add_query_param('SourceEndpoint.OracleSID',SourceEndpointOracleSID)

	def get_DestinationEndpointInstanceID(self):
		return self.get_query_params().get('DestinationEndpoint.InstanceID')

	def set_DestinationEndpointInstanceID(self,DestinationEndpointInstanceID):
		self.add_query_param('DestinationEndpoint.InstanceID',DestinationEndpointInstanceID)

	def get_SourceEndpointIP(self):
		return self.get_query_params().get('SourceEndpoint.IP')

	def set_SourceEndpointIP(self,SourceEndpointIP):
		self.add_query_param('SourceEndpoint.IP',SourceEndpointIP)

	def get_DestinationEndpointPassword(self):
		return self.get_query_params().get('DestinationEndpoint.Password')

	def set_DestinationEndpointPassword(self,DestinationEndpointPassword):
		self.add_query_param('DestinationEndpoint.Password',DestinationEndpointPassword)

	def get_MigrationObject(self):
		return self.get_query_params().get('MigrationObject')

	def set_MigrationObject(self,MigrationObject):
		self.add_query_param('MigrationObject',MigrationObject)

	def get_MigrationModeDataIntialization(self):
		return self.get_query_params().get('MigrationMode.DataIntialization')

	def set_MigrationModeDataIntialization(self,MigrationModeDataIntialization):
		self.add_query_param('MigrationMode.DataIntialization',MigrationModeDataIntialization)

	def get_MigrationJobId(self):
		return self.get_query_params().get('MigrationJobId')

	def set_MigrationJobId(self,MigrationJobId):
		self.add_query_param('MigrationJobId',MigrationJobId)

	def get_SourceEndpointInstanceType(self):
		return self.get_query_params().get('SourceEndpoint.InstanceType')

	def set_SourceEndpointInstanceType(self,SourceEndpointInstanceType):
		self.add_query_param('SourceEndpoint.InstanceType',SourceEndpointInstanceType)

	def get_DestinationEndpointEngineName(self):
		return self.get_query_params().get('DestinationEndpoint.EngineName')

	def set_DestinationEndpointEngineName(self,DestinationEndpointEngineName):
		self.add_query_param('DestinationEndpoint.EngineName',DestinationEndpointEngineName)

	def get_AccountId(self):
		return self.get_query_params().get('AccountId')

	def set_AccountId(self,AccountId):
		self.add_query_param('AccountId',AccountId)

	def get_MigrationModeStructureIntialization(self):
		return self.get_query_params().get('MigrationMode.StructureIntialization')

	def set_MigrationModeStructureIntialization(self,MigrationModeStructureIntialization):
		self.add_query_param('MigrationMode.StructureIntialization',MigrationModeStructureIntialization)

	def get_MigrationModeDataSynchronization(self):
		return self.get_query_params().get('MigrationMode.DataSynchronization')

	def set_MigrationModeDataSynchronization(self,MigrationModeDataSynchronization):
		self.add_query_param('MigrationMode.DataSynchronization',MigrationModeDataSynchronization)

	def get_DestinationEndpointRegion(self):
		return self.get_query_params().get('DestinationEndpoint.Region')

	def set_DestinationEndpointRegion(self,DestinationEndpointRegion):
		self.add_query_param('DestinationEndpoint.Region',DestinationEndpointRegion)

	def get_SourceEndpointUserName(self):
		return self.get_query_params().get('SourceEndpoint.UserName')

	def set_SourceEndpointUserName(self,SourceEndpointUserName):
		self.add_query_param('SourceEndpoint.UserName',SourceEndpointUserName)

	def get_SourceEndpointDatabaseName(self):
		return self.get_query_params().get('SourceEndpoint.DatabaseName')

	def set_SourceEndpointDatabaseName(self,SourceEndpointDatabaseName):
		self.add_query_param('SourceEndpoint.DatabaseName',SourceEndpointDatabaseName)

	def get_SourceEndpointPort(self):
		return self.get_query_params().get('SourceEndpoint.Port')

	def set_SourceEndpointPort(self,SourceEndpointPort):
		self.add_query_param('SourceEndpoint.Port',SourceEndpointPort)

	def get_SourceEndpointOwnerID(self):
		return self.get_query_params().get('SourceEndpoint.OwnerID')

	def set_SourceEndpointOwnerID(self,SourceEndpointOwnerID):
		self.add_query_param('SourceEndpoint.OwnerID',SourceEndpointOwnerID)

	def get_DestinationEndpointUserName(self):
		return self.get_query_params().get('DestinationEndpoint.UserName')

	def set_DestinationEndpointUserName(self,DestinationEndpointUserName):
		self.add_query_param('DestinationEndpoint.UserName',DestinationEndpointUserName)

	def get_DestinationEndpointOracleSID(self):
		return self.get_query_params().get('DestinationEndpoint.OracleSID')

	def set_DestinationEndpointOracleSID(self,DestinationEndpointOracleSID):
		self.add_query_param('DestinationEndpoint.OracleSID',DestinationEndpointOracleSID)

	def get_DestinationEndpointPort(self):
		return self.get_query_params().get('DestinationEndpoint.Port')

	def set_DestinationEndpointPort(self,DestinationEndpointPort):
		self.add_query_param('DestinationEndpoint.Port',DestinationEndpointPort)

	def get_SourceEndpointRegion(self):
		return self.get_query_params().get('SourceEndpoint.Region')

	def set_SourceEndpointRegion(self,SourceEndpointRegion):
		self.add_query_param('SourceEndpoint.Region',SourceEndpointRegion)

	def get_SourceEndpointRole(self):
		return self.get_query_params().get('SourceEndpoint.Role')

	def set_SourceEndpointRole(self,SourceEndpointRole):
		self.add_query_param('SourceEndpoint.Role',SourceEndpointRole)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DestinationEndpointDataBaseName(self):
		return self.get_query_params().get('DestinationEndpoint.DataBaseName')

	def set_DestinationEndpointDataBaseName(self,DestinationEndpointDataBaseName):
		self.add_query_param('DestinationEndpoint.DataBaseName',DestinationEndpointDataBaseName)

	def get_SourceEndpointPassword(self):
		return self.get_query_params().get('SourceEndpoint.Password')

	def set_SourceEndpointPassword(self,SourceEndpointPassword):
		self.add_query_param('SourceEndpoint.Password',SourceEndpointPassword)

	def get_MigrationReserved(self):
		return self.get_query_params().get('MigrationReserved')

	def set_MigrationReserved(self,MigrationReserved):
		self.add_query_param('MigrationReserved',MigrationReserved)

	def get_DestinationEndpointIP(self):
		return self.get_query_params().get('DestinationEndpoint.IP')

	def set_DestinationEndpointIP(self,DestinationEndpointIP):
		self.add_query_param('DestinationEndpoint.IP',DestinationEndpointIP)

	def get_MigrationJobName(self):
		return self.get_query_params().get('MigrationJobName')

	def set_MigrationJobName(self,MigrationJobName):
		self.add_query_param('MigrationJobName',MigrationJobName)

	def get_DestinationEndpointInstanceType(self):
		return self.get_query_params().get('DestinationEndpoint.InstanceType')

	def set_DestinationEndpointInstanceType(self,DestinationEndpointInstanceType):
		self.add_query_param('DestinationEndpoint.InstanceType',DestinationEndpointInstanceType)