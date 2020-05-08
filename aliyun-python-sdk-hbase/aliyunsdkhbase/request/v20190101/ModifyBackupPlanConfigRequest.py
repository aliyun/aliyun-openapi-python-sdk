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
from aliyunsdkhbase.endpoint import endpoint_data

class ModifyBackupPlanConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'ModifyBackupPlanConfig','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FullBackupCycle(self):
		return self.get_query_params().get('FullBackupCycle')

	def set_FullBackupCycle(self,FullBackupCycle):
		self.add_query_param('FullBackupCycle',FullBackupCycle)

	def get_Tables(self):
		return self.get_query_params().get('Tables')

	def set_Tables(self,Tables):
		self.add_query_param('Tables',Tables)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_MinHFileBackupCount(self):
		return self.get_query_params().get('MinHFileBackupCount')

	def set_MinHFileBackupCount(self,MinHFileBackupCount):
		self.add_query_param('MinHFileBackupCount',MinHFileBackupCount)

	def get_NextFullBackupDate(self):
		return self.get_query_params().get('NextFullBackupDate')

	def set_NextFullBackupDate(self,NextFullBackupDate):
		self.add_query_param('NextFullBackupDate',NextFullBackupDate)