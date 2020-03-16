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
from aliyunsdkdbs.endpoint import endpoint_data

class ModifyBackupSourceEndpointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dbs', '2019-03-06', 'ModifyBackupSourceEndpoint','cbs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SourceEndpointRegion(self):
		return self.get_query_params().get('SourceEndpointRegion')

	def set_SourceEndpointRegion(self,SourceEndpointRegion):
		self.add_query_param('SourceEndpointRegion',SourceEndpointRegion)

	def get_BackupGatewayId(self):
		return self.get_query_params().get('BackupGatewayId')

	def set_BackupGatewayId(self,BackupGatewayId):
		self.add_query_param('BackupGatewayId',BackupGatewayId)

	def get_SourceEndpointInstanceID(self):
		return self.get_query_params().get('SourceEndpointInstanceID')

	def set_SourceEndpointInstanceID(self,SourceEndpointInstanceID):
		self.add_query_param('SourceEndpointInstanceID',SourceEndpointInstanceID)

	def get_SourceEndpointUserName(self):
		return self.get_query_params().get('SourceEndpointUserName')

	def set_SourceEndpointUserName(self,SourceEndpointUserName):
		self.add_query_param('SourceEndpointUserName',SourceEndpointUserName)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_BackupPlanId(self):
		return self.get_query_params().get('BackupPlanId')

	def set_BackupPlanId(self,BackupPlanId):
		self.add_query_param('BackupPlanId',BackupPlanId)

	def get_SourceEndpointDatabaseName(self):
		return self.get_query_params().get('SourceEndpointDatabaseName')

	def set_SourceEndpointDatabaseName(self,SourceEndpointDatabaseName):
		self.add_query_param('SourceEndpointDatabaseName',SourceEndpointDatabaseName)

	def get_SourceEndpointIP(self):
		return self.get_query_params().get('SourceEndpointIP')

	def set_SourceEndpointIP(self,SourceEndpointIP):
		self.add_query_param('SourceEndpointIP',SourceEndpointIP)

	def get_SourceEndpointPassword(self):
		return self.get_query_params().get('SourceEndpointPassword')

	def set_SourceEndpointPassword(self,SourceEndpointPassword):
		self.add_query_param('SourceEndpointPassword',SourceEndpointPassword)

	def get_BackupObjects(self):
		return self.get_query_params().get('BackupObjects')

	def set_BackupObjects(self,BackupObjects):
		self.add_query_param('BackupObjects',BackupObjects)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SourceEndpointPort(self):
		return self.get_query_params().get('SourceEndpointPort')

	def set_SourceEndpointPort(self,SourceEndpointPort):
		self.add_query_param('SourceEndpointPort',SourceEndpointPort)

	def get_SourceEndpointInstanceType(self):
		return self.get_query_params().get('SourceEndpointInstanceType')

	def set_SourceEndpointInstanceType(self,SourceEndpointInstanceType):
		self.add_query_param('SourceEndpointInstanceType',SourceEndpointInstanceType)

	def get_SourceEndpointOracleSID(self):
		return self.get_query_params().get('SourceEndpointOracleSID')

	def set_SourceEndpointOracleSID(self,SourceEndpointOracleSID):
		self.add_query_param('SourceEndpointOracleSID',SourceEndpointOracleSID)