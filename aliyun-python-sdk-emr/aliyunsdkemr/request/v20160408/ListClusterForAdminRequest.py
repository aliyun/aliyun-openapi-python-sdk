# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ListClusterForAdminRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListClusterForAdmin')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_StatusLists(self):
		return self.get_query_params().get('StatusLists')

	def set_StatusLists(self,StatusLists):
		for i in range(len(StatusLists)):	
			if StatusLists[i] is not None:
				self.add_query_param('StatusList.' + str(i + 1) , StatusLists[i]);

	def get_FuzzyName(self):
		return self.get_query_params().get('FuzzyName')

	def set_FuzzyName(self,FuzzyName):
		self.add_query_param('FuzzyName',FuzzyName)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_EcmClusterIdLists(self):
		return self.get_query_params().get('EcmClusterIdLists')

	def set_EcmClusterIdLists(self,EcmClusterIdLists):
		for i in range(len(EcmClusterIdLists)):	
			if EcmClusterIdLists[i] is not None:
				self.add_query_param('EcmClusterIdList.' + str(i + 1) , EcmClusterIdLists[i]);

	def get_ClusterIdLists(self):
		return self.get_query_params().get('ClusterIdLists')

	def set_ClusterIdLists(self,ClusterIdLists):
		for i in range(len(ClusterIdLists)):	
			if ClusterIdLists[i] is not None:
				self.add_query_param('ClusterIdList.' + str(i + 1) , ClusterIdLists[i]);

	def get_PayTypeLists(self):
		return self.get_query_params().get('PayTypeLists')

	def set_PayTypeLists(self,PayTypeLists):
		for i in range(len(PayTypeLists)):	
			if PayTypeLists[i] is not None:
				self.add_query_param('PayTypeList.' + str(i + 1) , PayTypeLists[i]);

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EmrVersion(self):
		return self.get_query_params().get('EmrVersion')

	def set_EmrVersion(self,EmrVersion):
		self.add_query_param('EmrVersion',EmrVersion)

	def get_Resize(self):
		return self.get_query_params().get('Resize')

	def set_Resize(self,Resize):
		self.add_query_param('Resize',Resize)

	def get_ClusterTypeLists(self):
		return self.get_query_params().get('ClusterTypeLists')

	def set_ClusterTypeLists(self,ClusterTypeLists):
		for i in range(len(ClusterTypeLists)):	
			if ClusterTypeLists[i] is not None:
				self.add_query_param('ClusterTypeList.' + str(i + 1) , ClusterTypeLists[i]);