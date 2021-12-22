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
from aliyunsdkrsimganalys.endpoint import endpoint_data

class CreateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rsimganalys', '2019-08-01', 'CreateTask','rsimganalys')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Confidence(self):
		return self.get_query_params().get('Confidence')

	def set_Confidence(self,Confidence):
		self.add_query_param('Confidence',Confidence)

	def get_FilterValue(self):
		return self.get_query_params().get('FilterValue')

	def set_FilterValue(self,FilterValue):
		self.add_query_param('FilterValue',FilterValue)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ShpFilter(self):
		return self.get_query_params().get('ShpFilter')

	def set_ShpFilter(self,ShpFilter):
		self.add_query_param('ShpFilter',ShpFilter)

	def get_ProductType(self):
		return self.get_query_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_query_param('ProductType',ProductType)

	def get_ZoneList(self):
		return self.get_query_params().get('ZoneList')

	def set_ZoneList(self,ZoneList):
		self.add_query_param('ZoneList',ZoneList)

	def get_SrcImageId(self):
		return self.get_query_params().get('SrcImageId')

	def set_SrcImageId(self,SrcImageId):
		self.add_query_param('SrcImageId',SrcImageId)

	def get_Appkey(self):
		return self.get_query_params().get('Appkey')

	def set_Appkey(self,Appkey):
		self.add_query_param('Appkey',Appkey)

	def get_DstImageId(self):
		return self.get_query_params().get('DstImageId')

	def set_DstImageId(self,DstImageId):
		self.add_query_param('DstImageId',DstImageId)

	def get_JobName(self):
		return self.get_query_params().get('JobName')

	def set_JobName(self,JobName):
		self.add_query_param('JobName',JobName)