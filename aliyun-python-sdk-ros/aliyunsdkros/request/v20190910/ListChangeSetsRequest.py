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
from aliyunsdkros.endpoint import endpoint_data

class ListChangeSetsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'ListChangeSets','ROS')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StackId(self):
		return self.get_query_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_query_param('StackId',StackId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ExecutionStatuss(self):
		return self.get_query_params().get('ExecutionStatuss')

	def set_ExecutionStatuss(self,ExecutionStatuss):
		for i in range(len(ExecutionStatuss)):	
			if ExecutionStatuss[i] is not None:
				self.add_query_param('ExecutionStatus.' + str(i + 1) , ExecutionStatuss[i]);

	def get_ChangeSetNames(self):
		return self.get_query_params().get('ChangeSetNames')

	def set_ChangeSetNames(self,ChangeSetNames):
		for i in range(len(ChangeSetNames)):	
			if ChangeSetNames[i] is not None:
				self.add_query_param('ChangeSetName.' + str(i + 1) , ChangeSetNames[i]);

	def get_ChangeSetId(self):
		return self.get_query_params().get('ChangeSetId')

	def set_ChangeSetId(self,ChangeSetId):
		self.add_query_param('ChangeSetId',ChangeSetId)

	def get_Statuss(self):
		return self.get_query_params().get('Statuss')

	def set_Statuss(self,Statuss):
		for i in range(len(Statuss)):	
			if Statuss[i] is not None:
				self.add_query_param('Status.' + str(i + 1) , Statuss[i]);