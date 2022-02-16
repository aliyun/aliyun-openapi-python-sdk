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
from aliyunsdkemr.endpoint import endpoint_data

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'CreateCluster','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MainVersion(self):
		return self.get_query_params().get('MainVersion')

	def set_MainVersion(self,MainVersion):
		self.add_query_param('MainVersion',MainVersion)

	def get_NodeKeyPairName(self):
		return self.get_query_params().get('NodeKeyPairName')

	def set_NodeKeyPairName(self,NodeKeyPairName):
		self.add_query_param('NodeKeyPairName',NodeKeyPairName)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_MetaStoreType(self):
		return self.get_query_params().get('MetaStoreType')

	def set_MetaStoreType(self,MetaStoreType):
		self.add_query_param('MetaStoreType',MetaStoreType)

	def get_ReleaseVersion(self):
		return self.get_query_params().get('ReleaseVersion')

	def set_ReleaseVersion(self,ReleaseVersion):
		self.add_query_param('ReleaseVersion',ReleaseVersion)

	def get_DeployMode(self):
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self,DeployMode):
		self.add_query_param('DeployMode',DeployMode)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_ClickhouseConf(self):
		return self.get_query_params().get('ClickhouseConf')

	def set_ClickhouseConf(self,ClickhouseConf):
		self.add_query_param('ClickhouseConf',ClickhouseConf)

	def get_NodeGroups(self):
		return self.get_query_params().get('NodeGroups')

	def set_NodeGroups(self,NodeGroups):
		self.add_query_param('NodeGroups',NodeGroups)

	def get_MetaStoreConf(self):
		return self.get_query_params().get('MetaStoreConf')

	def set_MetaStoreConf(self,MetaStoreConf):
		self.add_query_param('MetaStoreConf',MetaStoreConf)

	def get_NodeRamRole(self):
		return self.get_query_params().get('NodeRamRole')

	def set_NodeRamRole(self,NodeRamRole):
		self.add_query_param('NodeRamRole',NodeRamRole)

	def get_MasterWithPublicIp(self):
		return self.get_query_params().get('MasterWithPublicIp')

	def set_MasterWithPublicIp(self,MasterWithPublicIp):
		self.add_query_param('MasterWithPublicIp',MasterWithPublicIp)

	def get_Users(self):
		return self.get_query_params().get('Users')

	def set_Users(self,Users):
		self.add_query_param('Users',Users)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_NodeAttributes(self):
		return self.get_query_params().get('NodeAttributes')

	def set_NodeAttributes(self,NodeAttributes):
		self.add_query_param('NodeAttributes',NodeAttributes)

	def get_NodeRootPassword(self):
		return self.get_query_params().get('NodeRootPassword')

	def set_NodeRootPassword(self,NodeRootPassword):
		self.add_query_param('NodeRootPassword',NodeRootPassword)

	def get_BootstrapScripts(self):
		return self.get_query_params().get('BootstrapScripts')

	def set_BootstrapScripts(self,BootstrapScripts):
		self.add_query_param('BootstrapScripts',BootstrapScripts)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SecurityMode(self):
		return self.get_query_params().get('SecurityMode')

	def set_SecurityMode(self,SecurityMode):
		self.add_query_param('SecurityMode',SecurityMode)

	def get_SubscriptionConfig(self):
		return self.get_query_params().get('SubscriptionConfig')

	def set_SubscriptionConfig(self,SubscriptionConfig):
		self.add_query_param('SubscriptionConfig',SubscriptionConfig)

	def get_EmrStudioConfigs(self):
		return self.get_query_params().get('EmrStudioConfigs')

	def set_EmrStudioConfigs(self,EmrStudioConfigs):
		self.add_query_param('EmrStudioConfigs',EmrStudioConfigs)

	def get_SlaveSecurityGroupId(self):
		return self.get_query_params().get('SlaveSecurityGroupId')

	def set_SlaveSecurityGroupId(self,SlaveSecurityGroupId):
		self.add_query_param('SlaveSecurityGroupId',SlaveSecurityGroupId)

	def get_OptionApplications(self):
		return self.get_query_params().get('OptionApplications')

	def set_OptionApplications(self,OptionApplications):
		self.add_query_param('OptionApplications',OptionApplications)

	def get_ApplicationConfigs(self):
		return self.get_query_params().get('ApplicationConfigs')

	def set_ApplicationConfigs(self,ApplicationConfigs):
		self.add_query_param('ApplicationConfigs',ApplicationConfigs)

	def get_ComponentLayouts(self):
		return self.get_query_params().get('ComponentLayouts')

	def set_ComponentLayouts(self,ComponentLayouts):
		self.add_query_param('ComponentLayouts',ComponentLayouts)

	def get_Promotions(self):
		return self.get_query_params().get('Promotions')

	def set_Promotions(self,Promotions):
		self.add_query_param('Promotions',Promotions)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_PaymentType(self):
		return self.get_query_params().get('PaymentType')

	def set_PaymentType(self,PaymentType):
		self.add_query_param('PaymentType',PaymentType)

	def get_Applications(self):
		return self.get_query_params().get('Applications')

	def set_Applications(self,Applications):
		self.add_query_param('Applications',Applications)