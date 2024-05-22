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

class UpdateBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'UpdateBackupPolicy','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_CrossRegionDataBackupRetention(self): # Integer
		return self.get_query_params().get('CrossRegionDataBackupRetention')

	def set_CrossRegionDataBackupRetention(self, CrossRegionDataBackupRetention):  # Integer
		self.add_query_param('CrossRegionDataBackupRetention', CrossRegionDataBackupRetention)
	def get_ForceCleanOnHighSpaceUsage(self): # Integer
		return self.get_query_params().get('ForceCleanOnHighSpaceUsage')

	def set_ForceCleanOnHighSpaceUsage(self, ForceCleanOnHighSpaceUsage):  # Integer
		self.add_query_param('ForceCleanOnHighSpaceUsage', ForceCleanOnHighSpaceUsage)
	def get_BackupPlanBegin(self): # String
		return self.get_query_params().get('BackupPlanBegin')

	def set_BackupPlanBegin(self, BackupPlanBegin):  # String
		self.add_query_param('BackupPlanBegin', BackupPlanBegin)
	def get_RemoveLogRetention(self): # Integer
		return self.get_query_params().get('RemoveLogRetention')

	def set_RemoveLogRetention(self, RemoveLogRetention):  # Integer
		self.add_query_param('RemoveLogRetention', RemoveLogRetention)
	def get_ColdDataBackupRetention(self): # Integer
		return self.get_query_params().get('ColdDataBackupRetention')

	def set_ColdDataBackupRetention(self, ColdDataBackupRetention):  # Integer
		self.add_query_param('ColdDataBackupRetention', ColdDataBackupRetention)
	def get_LocalLogRetentionNumber(self): # Integer
		return self.get_query_params().get('LocalLogRetentionNumber')

	def set_LocalLogRetentionNumber(self, LocalLogRetentionNumber):  # Integer
		self.add_query_param('LocalLogRetentionNumber', LocalLogRetentionNumber)
	def get_BackupType(self): # String
		return self.get_query_params().get('BackupType')

	def set_BackupType(self, BackupType):  # String
		self.add_query_param('BackupType', BackupType)
	def get_IsEnabled(self): # Integer
		return self.get_query_params().get('IsEnabled')

	def set_IsEnabled(self, IsEnabled):  # Integer
		self.add_query_param('IsEnabled', IsEnabled)
	def get_ColdDataBackupInterval(self): # Integer
		return self.get_query_params().get('ColdDataBackupInterval')

	def set_ColdDataBackupInterval(self, ColdDataBackupInterval):  # Integer
		self.add_query_param('ColdDataBackupInterval', ColdDataBackupInterval)
	def get_BackupWay(self): # String
		return self.get_query_params().get('BackupWay')

	def set_BackupWay(self, BackupWay):  # String
		self.add_query_param('BackupWay', BackupWay)
	def get_DestCrossRegion(self): # String
		return self.get_query_params().get('DestCrossRegion')

	def set_DestCrossRegion(self, DestCrossRegion):  # String
		self.add_query_param('DestCrossRegion', DestCrossRegion)
	def get_BackupSetRetention(self): # Integer
		return self.get_query_params().get('BackupSetRetention')

	def set_BackupSetRetention(self, BackupSetRetention):  # Integer
		self.add_query_param('BackupSetRetention', BackupSetRetention)
	def get_IsCrossRegionDataBackupEnabled(self): # Boolean
		return self.get_query_params().get('IsCrossRegionDataBackupEnabled')

	def set_IsCrossRegionDataBackupEnabled(self, IsCrossRegionDataBackupEnabled):  # Boolean
		self.add_query_param('IsCrossRegionDataBackupEnabled', IsCrossRegionDataBackupEnabled)
	def get_CrossRegionLogBackupRetention(self): # Integer
		return self.get_query_params().get('CrossRegionLogBackupRetention')

	def set_CrossRegionLogBackupRetention(self, CrossRegionLogBackupRetention):  # Integer
		self.add_query_param('CrossRegionLogBackupRetention', CrossRegionLogBackupRetention)
	def get_BackupPeriod(self): # String
		return self.get_query_params().get('BackupPeriod')

	def set_BackupPeriod(self, BackupPeriod):  # String
		self.add_query_param('BackupPeriod', BackupPeriod)
	def get_IsCrossRegionLogBackupEnabled(self): # Boolean
		return self.get_query_params().get('IsCrossRegionLogBackupEnabled')

	def set_IsCrossRegionLogBackupEnabled(self, IsCrossRegionLogBackupEnabled):  # Boolean
		self.add_query_param('IsCrossRegionLogBackupEnabled', IsCrossRegionLogBackupEnabled)
	def get_LocalLogRetention(self): # Integer
		return self.get_query_params().get('LocalLogRetention')

	def set_LocalLogRetention(self, LocalLogRetention):  # Integer
		self.add_query_param('LocalLogRetention', LocalLogRetention)
	def get_LogLocalRetentionSpace(self): # Integer
		return self.get_query_params().get('LogLocalRetentionSpace')

	def set_LogLocalRetentionSpace(self, LogLocalRetentionSpace):  # Integer
		self.add_query_param('LogLocalRetentionSpace', LogLocalRetentionSpace)
