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
from aliyunsdknas.endpoint import endpoint_data

class CreateDataFlowRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateDataFlow','nas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoRefreshPolicy(self):
		return self.get_query_params().get('AutoRefreshPolicy')

	def set_AutoRefreshPolicy(self,AutoRefreshPolicy):
		self.add_query_param('AutoRefreshPolicy',AutoRefreshPolicy)

	def get_FsetId(self):
		return self.get_query_params().get('FsetId')

	def set_FsetId(self,FsetId):
		self.add_query_param('FsetId',FsetId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AutoRefreshss(self):
		return self.get_query_params().get('AutoRefreshs')

	def set_AutoRefreshss(self, AutoRefreshss):
		for depth1 in range(len(AutoRefreshss)):
			if AutoRefreshss[depth1].get('RefreshPath') is not None:
				self.add_query_param('AutoRefreshs.' + str(depth1 + 1) + '.RefreshPath', AutoRefreshss[depth1].get('RefreshPath'))

	def get_SourceSecurityType(self):
		return self.get_query_params().get('SourceSecurityType')

	def set_SourceSecurityType(self,SourceSecurityType):
		self.add_query_param('SourceSecurityType',SourceSecurityType)

	def get_SourceStorage(self):
		return self.get_query_params().get('SourceStorage')

	def set_SourceStorage(self,SourceStorage):
		self.add_query_param('SourceStorage',SourceStorage)

	def get_Throughput(self):
		return self.get_query_params().get('Throughput')

	def set_Throughput(self,Throughput):
		self.add_query_param('Throughput',Throughput)

	def get_FileSystemId(self):
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self,FileSystemId):
		self.add_query_param('FileSystemId',FileSystemId)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_AutoRefreshInterval(self):
		return self.get_query_params().get('AutoRefreshInterval')

	def set_AutoRefreshInterval(self,AutoRefreshInterval):
		self.add_query_param('AutoRefreshInterval',AutoRefreshInterval)