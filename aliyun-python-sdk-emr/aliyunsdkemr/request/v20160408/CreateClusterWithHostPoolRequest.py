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

class CreateClusterWithHostPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateClusterWithHostPool','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_EasEnable(self):
		return self.get_query_params().get('EasEnable')

	def set_EasEnable(self,EasEnable):
		self.add_query_param('EasEnable',EasEnable)

	def get_HostInfos(self):
		return self.get_query_params().get('HostInfos')

	def set_HostInfos(self,HostInfos):
		for i in range(len(HostInfos)):	
			if HostInfos[i].get('HpHostBizId') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.HpHostBizId' , HostInfos[i].get('HpHostBizId'))
			if HostInfos[i].get('HostName') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.HostName' , HostInfos[i].get('HostName'))
			if HostInfos[i].get('Role') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.Role' , HostInfos[i].get('Role'))
			if HostInfos[i].get('GroupId') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.GroupId' , HostInfos[i].get('GroupId'))
			if HostInfos[i].get('PrivateIp') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.PrivateIp' , HostInfos[i].get('PrivateIp'))
			for j in range(len(HostInfos[i].get('ServiceComponentInfos'))):
				if HostInfos[i].get('ServiceComponentInfos')[j] is not None:
					self.add_query_param('HostInfo.' + str(i + 1) + '.ServiceComponentInfo.'+str(j + 1), HostInfos[i].get('ServiceComponentInfos')[j])
			if HostInfos[i].get('HostGroupName') is not None:
				self.add_query_param('HostInfo.' + str(i + 1) + '.HostGroupName' , HostInfos[i].get('HostGroupName'))


	def get_RelatedClusterId(self):
		return self.get_query_params().get('RelatedClusterId')

	def set_RelatedClusterId(self,RelatedClusterId):
		self.add_query_param('RelatedClusterId',RelatedClusterId)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_HostGroups(self):
		return self.get_query_params().get('HostGroups')

	def set_HostGroups(self,HostGroups):
		for i in range(len(HostGroups)):	
			if HostGroups[i].get('GroupType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.GroupType' , HostGroups[i].get('GroupType'))
			if HostGroups[i].get('GroupId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.GroupId' , HostGroups[i].get('GroupId'))
			if HostGroups[i].get('GroupName') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.GroupName' , HostGroups[i].get('GroupName'))


	def get_StackName(self):
		return self.get_query_params().get('StackName')

	def set_StackName(self,StackName):
		self.add_query_param('StackName',StackName)

	def get_StackVersion(self):
		return self.get_query_params().get('StackVersion')

	def set_StackVersion(self,StackVersion):
		self.add_query_param('StackVersion',StackVersion)

	def get_ServiceInfos(self):
		return self.get_query_params().get('ServiceInfos')

	def set_ServiceInfos(self,ServiceInfos):
		for i in range(len(ServiceInfos)):	
			if ServiceInfos[i].get('ServiceEcmVersion') is not None:
				self.add_query_param('ServiceInfo.' + str(i + 1) + '.ServiceEcmVersion' , ServiceInfos[i].get('ServiceEcmVersion'))
			if ServiceInfos[i].get('ServiceVersion') is not None:
				self.add_query_param('ServiceInfo.' + str(i + 1) + '.ServiceVersion' , ServiceInfos[i].get('ServiceVersion'))
			if ServiceInfos[i].get('ServiceName') is not None:
				self.add_query_param('ServiceInfo.' + str(i + 1) + '.ServiceName' , ServiceInfos[i].get('ServiceName'))


	def get_Configs(self):
		return self.get_query_params().get('Configs')

	def set_Configs(self,Configs):
		for i in range(len(Configs)):	
			if Configs[i].get('ConfigKey') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigKey' , Configs[i].get('ConfigKey'))
			if Configs[i].get('FileName') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.FileName' , Configs[i].get('FileName'))
			if Configs[i].get('ConfigValue') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigValue' , Configs[i].get('ConfigValue'))
			if Configs[i].get('ServiceName') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ServiceName' , Configs[i].get('ServiceName'))
