# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Yundun-ds', '2019-01-03', 'DescribeEvents','sddp')

	def get_FeatureType(self):
		return self.get_query_params().get('FeatureType')

	def set_FeatureType(self,FeatureType):
		self.add_query_param('FeatureType',FeatureType)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_TypeCode(self):
		return self.get_query_params().get('TypeCode')

	def set_TypeCode(self,TypeCode):
		self.add_query_param('TypeCode',TypeCode)

	def get_SubTypeCode(self):
		return self.get_query_params().get('SubTypeCode')

	def set_SubTypeCode(self,SubTypeCode):
		self.add_query_param('SubTypeCode',SubTypeCode)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DepartId(self):
		return self.get_query_params().get('DepartId')

	def set_DepartId(self,DepartId):
		self.add_query_param('DepartId',DepartId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_DealUserId(self):
		return self.get_query_params().get('DealUserId')

	def set_DealUserId(self,DealUserId):
		self.add_query_param('DealUserId',DealUserId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)