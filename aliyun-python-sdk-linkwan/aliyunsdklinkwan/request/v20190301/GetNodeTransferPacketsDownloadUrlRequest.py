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
from aliyunsdklinkwan.endpoint import endpoint_data

class GetNodeTransferPacketsDownloadUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'GetNodeTransferPacketsDownloadUrl','linkwan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndMillis(self):
		return self.get_query_params().get('EndMillis')

	def set_EndMillis(self,EndMillis):
		self.add_query_param('EndMillis',EndMillis)

	def get_GwEui(self):
		return self.get_query_params().get('GwEui')

	def set_GwEui(self,GwEui):
		self.add_query_param('GwEui',GwEui)

	def get_Ascending(self):
		return self.get_query_params().get('Ascending')

	def set_Ascending(self,Ascending):
		self.add_query_param('Ascending',Ascending)

	def get_DevEui(self):
		return self.get_query_params().get('DevEui')

	def set_DevEui(self,DevEui):
		self.add_query_param('DevEui',DevEui)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_BeginMillis(self):
		return self.get_query_params().get('BeginMillis')

	def set_BeginMillis(self,BeginMillis):
		self.add_query_param('BeginMillis',BeginMillis)

	def get_SortingField(self):
		return self.get_query_params().get('SortingField')

	def set_SortingField(self,SortingField):
		self.add_query_param('SortingField',SortingField)