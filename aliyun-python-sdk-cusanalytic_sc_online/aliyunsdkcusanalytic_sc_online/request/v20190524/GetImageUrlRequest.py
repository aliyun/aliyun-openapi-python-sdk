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
from aliyunsdkcusanalytic_sc_online.endpoint import endpoint_data

class GetImageUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cusanalytic_sc_online', '2019-05-24', 'GetImageUrl')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OriginUrls(self):
		return self.get_body_params().get('OriginUrls')

	def set_OriginUrls(self,OriginUrls):
		self.add_body_params('OriginUrls', OriginUrls)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_ObjectKeys(self):
		return self.get_body_params().get('ObjectKeys')

	def set_ObjectKeys(self,ObjectKeys):
		self.add_body_params('ObjectKeys', ObjectKeys)