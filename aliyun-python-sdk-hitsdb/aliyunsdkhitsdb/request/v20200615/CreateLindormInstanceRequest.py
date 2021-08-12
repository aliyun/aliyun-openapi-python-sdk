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

class CreateLindormInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hitsdb', '2020-06-15', 'CreateLindormInstance','hitsdb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TsdbSpec(self):
		return self.get_query_params().get('TsdbSpec')

	def set_TsdbSpec(self,TsdbSpec):
		self.add_query_param('TsdbSpec',TsdbSpec)

	def get_FilestoreSpec(self):
		return self.get_query_params().get('FilestoreSpec')

	def set_FilestoreSpec(self,FilestoreSpec):
		self.add_query_param('FilestoreSpec',FilestoreSpec)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_TsdbNum(self):
		return self.get_query_params().get('TsdbNum')

	def set_TsdbNum(self,TsdbNum):
		self.add_query_param('TsdbNum',TsdbNum)

	def get_DiskCategory(self):
		return self.get_query_params().get('DiskCategory')

	def set_DiskCategory(self,DiskCategory):
		self.add_query_param('DiskCategory',DiskCategory)

	def get_LindormSpec(self):
		return self.get_query_params().get('LindormSpec')

	def set_LindormSpec(self,LindormSpec):
		self.add_query_param('LindormSpec',LindormSpec)

	def get_SolrNum(self):
		return self.get_query_params().get('SolrNum')

	def set_SolrNum(self,SolrNum):
		self.add_query_param('SolrNum',SolrNum)

	def get_ColdStorage(self):
		return self.get_query_params().get('ColdStorage')

	def set_ColdStorage(self,ColdStorage):
		self.add_query_param('ColdStorage',ColdStorage)

	def get_InstanceStorage(self):
		return self.get_query_params().get('InstanceStorage')

	def set_InstanceStorage(self,InstanceStorage):
		self.add_query_param('InstanceStorage',InstanceStorage)

	def get_SolrSpec(self):
		return self.get_query_params().get('SolrSpec')

	def set_SolrSpec(self,SolrSpec):
		self.add_query_param('SolrSpec',SolrSpec)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceAlias(self):
		return self.get_query_params().get('InstanceAlias')

	def set_InstanceAlias(self,InstanceAlias):
		self.add_query_param('InstanceAlias',InstanceAlias)

	def get_FilestoreNum(self):
		return self.get_query_params().get('FilestoreNum')

	def set_FilestoreNum(self,FilestoreNum):
		self.add_query_param('FilestoreNum',FilestoreNum)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LindormNum(self):
		return self.get_query_params().get('LindormNum')

	def set_LindormNum(self,LindormNum):
		self.add_query_param('LindormNum',LindormNum)

	def get_CoreSpec(self):
		return self.get_query_params().get('CoreSpec')

	def set_CoreSpec(self,CoreSpec):
		self.add_query_param('CoreSpec',CoreSpec)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)