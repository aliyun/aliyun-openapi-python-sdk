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
from aliyunsdkretailcloud.endpoint import endpoint_data

class ListSlbAPsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'ListSlbAPs','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProtocolLists(self):
		return self.get_body_params().get('ProtocolLists')

	def set_ProtocolLists(self,ProtocolLists):
		for i in range(len(ProtocolLists)):	
			if ProtocolLists[i] is not None:
				self.add_body_params('ProtocolList.' + str(i + 1) , ProtocolLists[i]);

	def get_SlbId(self):
		return self.get_query_params().get('SlbId')

	def set_SlbId(self,SlbId):
		self.add_query_param('SlbId',SlbId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)

	def get_NetworkMode(self):
		return self.get_query_params().get('NetworkMode')

	def set_NetworkMode(self,NetworkMode):
		self.add_query_param('NetworkMode',NetworkMode)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)