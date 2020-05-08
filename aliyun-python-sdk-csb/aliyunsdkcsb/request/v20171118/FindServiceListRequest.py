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
from aliyunsdkcsb.endpoint import endpoint_data

class FindServiceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CSB', '2017-11-18', 'FindServiceList')
		self.set_protocol_type('https')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectName(self):
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_query_param('ProjectName',ProjectName)

	def get_ShowDelService(self):
		return self.get_query_params().get('ShowDelService')

	def set_ShowDelService(self,ShowDelService):
		self.add_query_param('ShowDelService',ShowDelService)

	def get_CsbId(self):
		return self.get_query_params().get('CsbId')

	def set_CsbId(self,CsbId):
		self.add_query_param('CsbId',CsbId)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_CasShowType(self):
		return self.get_query_params().get('CasShowType')

	def set_CasShowType(self,CasShowType):
		self.add_query_param('CasShowType',CasShowType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Alias(self):
		return self.get_query_params().get('Alias')

	def set_Alias(self,Alias):
		self.add_query_param('Alias',Alias)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)