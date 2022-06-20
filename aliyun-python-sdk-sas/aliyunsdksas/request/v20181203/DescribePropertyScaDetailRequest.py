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
from aliyunsdksas.endpoint import endpoint_data

class DescribePropertyScaDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribePropertyScaDetail')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SearchItemSub(self): # String
		return self.get_query_params().get('SearchItemSub')

	def set_SearchItemSub(self, SearchItemSub):  # String
		self.add_query_param('SearchItemSub', SearchItemSub)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Pid(self): # String
		return self.get_query_params().get('Pid')

	def set_Pid(self, Pid):  # String
		self.add_query_param('Pid', Pid)
	def get_SearchItem(self): # String
		return self.get_query_params().get('SearchItem')

	def set_SearchItem(self, SearchItem):  # String
		self.add_query_param('SearchItem', SearchItem)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_Biz(self): # String
		return self.get_query_params().get('Biz')

	def set_Biz(self, Biz):  # String
		self.add_query_param('Biz', Biz)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ProcessStartedStart(self): # Long
		return self.get_query_params().get('ProcessStartedStart')

	def set_ProcessStartedStart(self, ProcessStartedStart):  # Long
		self.add_query_param('ProcessStartedStart', ProcessStartedStart)
	def get_ProcessStartedEnd(self): # Long
		return self.get_query_params().get('ProcessStartedEnd')

	def set_ProcessStartedEnd(self, ProcessStartedEnd):  # Long
		self.add_query_param('ProcessStartedEnd', ProcessStartedEnd)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ScaVersion(self): # String
		return self.get_query_params().get('ScaVersion')

	def set_ScaVersion(self, ScaVersion):  # String
		self.add_query_param('ScaVersion', ScaVersion)
	def get_SearchInfoSub(self): # String
		return self.get_query_params().get('SearchInfoSub')

	def set_SearchInfoSub(self, SearchInfoSub):  # String
		self.add_query_param('SearchInfoSub', SearchInfoSub)
	def get_SearchInfo(self): # String
		return self.get_query_params().get('SearchInfo')

	def set_SearchInfo(self, SearchInfo):  # String
		self.add_query_param('SearchInfo', SearchInfo)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_Port(self): # String
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # String
		self.add_query_param('Port', Port)
	def get_Name(self): # Long
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # Long
		self.add_query_param('Name', Name)
	def get_ScaName(self): # String
		return self.get_query_params().get('ScaName')

	def set_ScaName(self, ScaName):  # String
		self.add_query_param('ScaName', ScaName)
	def get_ScaNamePattern(self): # String
		return self.get_query_params().get('ScaNamePattern')

	def set_ScaNamePattern(self, ScaNamePattern):  # String
		self.add_query_param('ScaNamePattern', ScaNamePattern)
	def get_User(self): # String
		return self.get_query_params().get('User')

	def set_User(self, User):  # String
		self.add_query_param('User', User)
