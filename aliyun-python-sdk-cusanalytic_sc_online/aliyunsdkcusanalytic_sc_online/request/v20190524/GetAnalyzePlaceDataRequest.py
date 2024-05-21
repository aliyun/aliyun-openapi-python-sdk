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

class GetAnalyzePlaceDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cusanalytic_sc_online', '2019-05-24', 'GetAnalyzePlaceData')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndUVCount(self):
		return self.get_body_params().get('EndUVCount')

	def set_EndUVCount(self,EndUVCount):
		self.add_body_params('EndUVCount', EndUVCount)

	def get_ParentAmount(self):
		return self.get_body_params().get('ParentAmount')

	def set_ParentAmount(self,ParentAmount):
		self.add_body_params('ParentAmount', ParentAmount)

	def get_StartDate(self):
		return self.get_body_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_body_params('StartDate', StartDate)

	def get_StartUVCount(self):
		return self.get_body_params().get('StartUVCount')

	def set_StartUVCount(self,StartUVCount):
		self.add_body_params('StartUVCount', StartUVCount)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_EndDate(self):
		return self.get_body_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_body_params('EndDate', EndDate)

	def get_LocationId(self):
		return self.get_body_params().get('LocationId')

	def set_LocationId(self,LocationId):
		self.add_body_params('LocationId', LocationId)

	def get_ParentLocationIds(self):
		return self.get_body_params().get('ParentLocationIds')

	def set_ParentLocationIds(self,ParentLocationIds):
		self.add_body_params('ParentLocationIds', ParentLocationIds)