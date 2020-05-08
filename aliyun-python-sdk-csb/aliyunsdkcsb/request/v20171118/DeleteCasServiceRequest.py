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

class DeleteCasServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CSB', '2017-11-18', 'DeleteCasService')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LeafOnly(self):
		return self.get_query_params().get('LeafOnly')

	def set_LeafOnly(self,LeafOnly):
		self.add_query_param('LeafOnly',LeafOnly)

	def get_CasCsbName(self):
		return self.get_query_params().get('CasCsbName')

	def set_CasCsbName(self,CasCsbName):
		self.add_query_param('CasCsbName',CasCsbName)

	def get_SrcUserId(self):
		return self.get_query_params().get('SrcUserId')

	def set_SrcUserId(self,SrcUserId):
		self.add_query_param('SrcUserId',SrcUserId)

	def get_CasServiceId(self):
		return self.get_query_params().get('CasServiceId')

	def set_CasServiceId(self,CasServiceId):
		self.add_query_param('CasServiceId',CasServiceId)