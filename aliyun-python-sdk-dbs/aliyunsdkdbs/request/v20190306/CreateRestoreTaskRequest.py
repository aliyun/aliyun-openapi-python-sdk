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

class CreateRestoreTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dbs', '2019-03-06', 'CreateRestoreTask','cbs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BackupGatewayId(self): # Long
		return self.get_query_params().get('BackupGatewayId')

	def set_BackupGatewayId(self, BackupGatewayId):  # Long
		self.add_query_param('BackupGatewayId', BackupGatewayId)
	def get_CrossRoleName(self): # String
		return self.get_query_params().get('CrossRoleName')

	def set_CrossRoleName(self, CrossRoleName):  # String
		self.add_query_param('CrossRoleName', CrossRoleName)
	def get_DestinationEndpointUserName(self): # String
		return self.get_query_params().get('DestinationEndpointUserName')

	def set_DestinationEndpointUserName(self, DestinationEndpointUserName):  # String
		self.add_query_param('DestinationEndpointUserName', DestinationEndpointUserName)
	def get_RestoreTaskName(self): # String
		return self.get_query_params().get('RestoreTaskName')

	def set_RestoreTaskName(self, RestoreTaskName):  # String
		self.add_query_param('RestoreTaskName', RestoreTaskName)
	def get_DestinationEndpointOracleSID(self): # String
		return self.get_query_params().get('DestinationEndpointOracleSID')

	def set_DestinationEndpointOracleSID(self, DestinationEndpointOracleSID):  # String
		self.add_query_param('DestinationEndpointOracleSID', DestinationEndpointOracleSID)
	def get_DestinationEndpointPort(self): # Integer
		return self.get_query_params().get('DestinationEndpointPort')

	def set_DestinationEndpointPort(self, DestinationEndpointPort):  # Integer
		self.add_query_param('DestinationEndpointPort', DestinationEndpointPort)
	def get_BackupSetId(self): # String
		return self.get_query_params().get('BackupSetId')

	def set_BackupSetId(self, BackupSetId):  # String
		self.add_query_param('BackupSetId', BackupSetId)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_RestoreDir(self): # String
		return self.get_query_params().get('RestoreDir')

	def set_RestoreDir(self, RestoreDir):  # String
		self.add_query_param('RestoreDir', RestoreDir)
	def get_DestinationEndpointIP(self): # String
		return self.get_query_params().get('DestinationEndpointIP')

	def set_DestinationEndpointIP(self, DestinationEndpointIP):  # String
		self.add_query_param('DestinationEndpointIP', DestinationEndpointIP)
	def get_DuplicateConflict(self): # String
		return self.get_query_params().get('DuplicateConflict')

	def set_DuplicateConflict(self, DuplicateConflict):  # String
		self.add_query_param('DuplicateConflict', DuplicateConflict)
	def get_DestinationEndpointInstanceType(self): # String
		return self.get_query_params().get('DestinationEndpointInstanceType')

	def set_DestinationEndpointInstanceType(self, DestinationEndpointInstanceType):  # String
		self.add_query_param('DestinationEndpointInstanceType', DestinationEndpointInstanceType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BackupPlanId(self): # String
		return self.get_query_params().get('BackupPlanId')

	def set_BackupPlanId(self, BackupPlanId):  # String
		self.add_query_param('BackupPlanId', BackupPlanId)
	def get_DestinationEndpointRegion(self): # String
		return self.get_query_params().get('DestinationEndpointRegion')

	def set_DestinationEndpointRegion(self, DestinationEndpointRegion):  # String
		self.add_query_param('DestinationEndpointRegion', DestinationEndpointRegion)
	def get_RestoreObjects(self): # String
		return self.get_query_params().get('RestoreObjects')

	def set_RestoreObjects(self, RestoreObjects):  # String
		self.add_query_param('RestoreObjects', RestoreObjects)
	def get_RestoreHome(self): # String
		return self.get_query_params().get('RestoreHome')

	def set_RestoreHome(self, RestoreHome):  # String
		self.add_query_param('RestoreHome', RestoreHome)
	def get_RestoreTime(self): # Long
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self, RestoreTime):  # Long
		self.add_query_param('RestoreTime', RestoreTime)
	def get_CrossAliyunId(self): # String
		return self.get_query_params().get('CrossAliyunId')

	def set_CrossAliyunId(self, CrossAliyunId):  # String
		self.add_query_param('CrossAliyunId', CrossAliyunId)
	def get_DestinationEndpointInstanceID(self): # String
		return self.get_query_params().get('DestinationEndpointInstanceID')

	def set_DestinationEndpointInstanceID(self, DestinationEndpointInstanceID):  # String
		self.add_query_param('DestinationEndpointInstanceID', DestinationEndpointInstanceID)
	def get_DestinationEndpointDatabaseName(self): # String
		return self.get_query_params().get('DestinationEndpointDatabaseName')

	def set_DestinationEndpointDatabaseName(self, DestinationEndpointDatabaseName):  # String
		self.add_query_param('DestinationEndpointDatabaseName', DestinationEndpointDatabaseName)
	def get_DestinationEndpointPassword(self): # String
		return self.get_query_params().get('DestinationEndpointPassword')

	def set_DestinationEndpointPassword(self, DestinationEndpointPassword):  # String
		self.add_query_param('DestinationEndpointPassword', DestinationEndpointPassword)
