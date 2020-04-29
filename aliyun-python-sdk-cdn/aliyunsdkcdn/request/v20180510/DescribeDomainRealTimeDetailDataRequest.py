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
from aliyunsdkcdn.endpoint import endpoint_data

class DescribeDomainRealTimeDetailDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'DescribeDomainRealTimeDetailData')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LocationNameEn(self):
		return self.get_query_params().get('LocationNameEn')

	def set_LocationNameEn(self,LocationNameEn):
		self.add_query_param('LocationNameEn',LocationNameEn)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_IspNameEn(self):
		return self.get_query_params().get('IspNameEn')

	def set_IspNameEn(self,IspNameEn):
		self.add_query_param('IspNameEn',IspNameEn)

	def get_Merge(self):
		return self.get_query_params().get('Merge')

	def set_Merge(self,Merge):
		self.add_query_param('Merge',Merge)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_MergeLocIsp(self):
		return self.get_query_params().get('MergeLocIsp')

	def set_MergeLocIsp(self,MergeLocIsp):
		self.add_query_param('MergeLocIsp',MergeLocIsp)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Field(self):
		return self.get_query_params().get('Field')

	def set_Field(self,Field):
		self.add_query_param('Field',Field)