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

class CreateHostPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateHostPool','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_KubeClusterInfos(self):
		return self.get_query_params().get('KubeClusterInfos')

	def set_KubeClusterInfos(self,KubeClusterInfos):
		for i in range(len(KubeClusterInfos)):	
			if KubeClusterInfos[i].get('ExternalKey') is not None:
				self.add_query_param('KubeClusterInfo.' + str(i + 1) + '.ExternalKey' , KubeClusterInfos[i].get('ExternalKey'))
			if KubeClusterInfos[i].get('InternalConfig') is not None:
				self.add_query_param('KubeClusterInfo.' + str(i + 1) + '.InternalConfig' , KubeClusterInfos[i].get('InternalConfig'))
			if KubeClusterInfos[i].get('PublicConfig') is not None:
				self.add_query_param('KubeClusterInfo.' + str(i + 1) + '.PublicConfig' , KubeClusterInfos[i].get('PublicConfig'))
			if KubeClusterInfos[i].get('SshConfig') is not None:
				self.add_query_param('KubeClusterInfo.' + str(i + 1) + '.SshConfig' , KubeClusterInfos[i].get('SshConfig'))


	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)