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
from aliyunsdkhitsdb.endpoint import endpoint_data

class UpgradeLindormInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hitsdb', '2020-06-15', 'UpgradeLindormInstance','hitsdb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_LogSpec(self): # String
		return self.get_query_params().get('LogSpec')

	def set_LogSpec(self, LogSpec):  # String
		self.add_query_param('LogSpec', LogSpec)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_TsdbNum(self): # Integer
		return self.get_query_params().get('TsdbNum')

	def set_TsdbNum(self, TsdbNum):  # Integer
		self.add_query_param('TsdbNum', TsdbNum)
	def get_SolrNum(self): # Integer
		return self.get_query_params().get('SolrNum')

	def set_SolrNum(self, SolrNum):  # Integer
		self.add_query_param('SolrNum', SolrNum)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LindormNum(self): # Integer
		return self.get_query_params().get('LindormNum')

	def set_LindormNum(self, LindormNum):  # Integer
		self.add_query_param('LindormNum', LindormNum)
	def get_LtsCoreNum(self): # Integer
		return self.get_query_params().get('LtsCoreNum')

	def set_LtsCoreNum(self, LtsCoreNum):  # Integer
		self.add_query_param('LtsCoreNum', LtsCoreNum)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_StreamNum(self): # Integer
		return self.get_query_params().get('StreamNum')

	def set_StreamNum(self, StreamNum):  # Integer
		self.add_query_param('StreamNum', StreamNum)
	def get_LogSingleStorage(self): # Integer
		return self.get_query_params().get('LogSingleStorage')

	def set_LogSingleStorage(self, LogSingleStorage):  # Integer
		self.add_query_param('LogSingleStorage', LogSingleStorage)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_UpgradeType(self): # String
		return self.get_query_params().get('UpgradeType')

	def set_UpgradeType(self, UpgradeType):  # String
		self.add_query_param('UpgradeType', UpgradeType)
	def get_TsdbSpec(self): # String
		return self.get_query_params().get('TsdbSpec')

	def set_TsdbSpec(self, TsdbSpec):  # String
		self.add_query_param('TsdbSpec', TsdbSpec)
	def get_FilestoreSpec(self): # String
		return self.get_query_params().get('FilestoreSpec')

	def set_FilestoreSpec(self, FilestoreSpec):  # String
		self.add_query_param('FilestoreSpec', FilestoreSpec)
	def get_LindormSpec(self): # String
		return self.get_query_params().get('LindormSpec')

	def set_LindormSpec(self, LindormSpec):  # String
		self.add_query_param('LindormSpec', LindormSpec)
	def get_ColdStorage(self): # Integer
		return self.get_query_params().get('ColdStorage')

	def set_ColdStorage(self, ColdStorage):  # Integer
		self.add_query_param('ColdStorage', ColdStorage)
	def get_LogNum(self): # Integer
		return self.get_query_params().get('LogNum')

	def set_LogNum(self, LogNum):  # Integer
		self.add_query_param('LogNum', LogNum)
	def get_SolrSpec(self): # String
		return self.get_query_params().get('SolrSpec')

	def set_SolrSpec(self, SolrSpec):  # String
		self.add_query_param('SolrSpec', SolrSpec)
	def get_CoreSingleStorage(self): # Integer
		return self.get_query_params().get('CoreSingleStorage')

	def set_CoreSingleStorage(self, CoreSingleStorage):  # Integer
		self.add_query_param('CoreSingleStorage', CoreSingleStorage)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_FilestoreNum(self): # Integer
		return self.get_query_params().get('FilestoreNum')

	def set_FilestoreNum(self, FilestoreNum):  # Integer
		self.add_query_param('FilestoreNum', FilestoreNum)
	def get_StreamSpec(self): # String
		return self.get_query_params().get('StreamSpec')

	def set_StreamSpec(self, StreamSpec):  # String
		self.add_query_param('StreamSpec', StreamSpec)
	def get_LtsCoreSpec(self): # String
		return self.get_query_params().get('LtsCoreSpec')

	def set_LtsCoreSpec(self, LtsCoreSpec):  # String
		self.add_query_param('LtsCoreSpec', LtsCoreSpec)
	def get_ClusterStorage(self): # Integer
		return self.get_query_params().get('ClusterStorage')

	def set_ClusterStorage(self, ClusterStorage):  # Integer
		self.add_query_param('ClusterStorage', ClusterStorage)
