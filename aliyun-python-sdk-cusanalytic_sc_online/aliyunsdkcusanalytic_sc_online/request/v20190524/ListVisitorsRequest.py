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

class ListVisitorsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cusanalytic_sc_online', '2019-05-24', 'ListVisitors')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Gender(self):
		return self.get_body_params().get('Gender')

	def set_Gender(self,Gender):
		self.add_body_params('Gender', Gender)

	def get_UkId(self):
		return self.get_body_params().get('UkId')

	def set_UkId(self,UkId):
		self.add_body_params('UkId', UkId)

	def get_LocationIds(self):
		return self.get_body_params().get('LocationIds')

	def set_LocationIds(self,LocationIds):
		self.add_body_params('LocationIds', LocationIds)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_EnterCount(self):
		return self.get_body_params().get('EnterCount')

	def set_EnterCount(self,EnterCount):
		self.add_body_params('EnterCount', EnterCount)

	def get_PageIndex(self):
		return self.get_body_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_body_params('PageIndex', PageIndex)

	def get_AgeStart(self):
		return self.get_body_params().get('AgeStart')

	def set_AgeStart(self,AgeStart):
		self.add_body_params('AgeStart', AgeStart)

	def get_AgeEnd(self):
		return self.get_body_params().get('AgeEnd')

	def set_AgeEnd(self,AgeEnd):
		self.add_body_params('AgeEnd', AgeEnd)

	def get_PkId(self):
		return self.get_body_params().get('PkId')

	def set_PkId(self,PkId):
		self.add_body_params('PkId', PkId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_StoreIds(self):
		return self.get_body_params().get('StoreIds')

	def set_StoreIds(self,StoreIds):
		self.add_body_params('StoreIds', StoreIds)