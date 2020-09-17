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
from aliyunsdkalimt.endpoint import endpoint_data

class GetTitleIntelligenceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2018-10-12', 'GetTitleIntelligence','alimt')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CatLevelThreeId(self):
		return self.get_body_params().get('CatLevelThreeId')

	def set_CatLevelThreeId(self,CatLevelThreeId):
		self.add_body_params('CatLevelThreeId', CatLevelThreeId)

	def get_CatLevelTwoId(self):
		return self.get_body_params().get('CatLevelTwoId')

	def set_CatLevelTwoId(self,CatLevelTwoId):
		self.add_body_params('CatLevelTwoId', CatLevelTwoId)

	def get_Keywords(self):
		return self.get_body_params().get('Keywords')

	def set_Keywords(self,Keywords):
		self.add_body_params('Keywords', Keywords)

	def get_Platform(self):
		return self.get_body_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_body_params('Platform', Platform)

	def get_Extra(self):
		return self.get_body_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_body_params('Extra', Extra)