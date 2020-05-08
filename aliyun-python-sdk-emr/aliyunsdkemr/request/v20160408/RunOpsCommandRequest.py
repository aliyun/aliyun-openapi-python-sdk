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

class RunOpsCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'RunOpsCommand','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OpsCommandName(self):
		return self.get_query_params().get('OpsCommandName')

	def set_OpsCommandName(self,OpsCommandName):
		self.add_query_param('OpsCommandName',OpsCommandName)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)

	def get_CustomParams(self):
		return self.get_query_params().get('CustomParams')

	def set_CustomParams(self,CustomParams):
		self.add_query_param('CustomParams',CustomParams)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_HostIdLists(self):
		return self.get_query_params().get('HostIdLists')

	def set_HostIdLists(self,HostIdLists):
		for i in range(len(HostIdLists)):	
			if HostIdLists[i] is not None:
				self.add_query_param('HostIdList.' + str(i + 1) , HostIdLists[i]);

	def get_Dimension(self):
		return self.get_query_params().get('Dimension')

	def set_Dimension(self,Dimension):
		self.add_query_param('Dimension',Dimension)