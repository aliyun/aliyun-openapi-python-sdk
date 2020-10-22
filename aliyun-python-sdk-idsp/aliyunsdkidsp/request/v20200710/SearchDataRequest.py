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
from aliyunsdkidsp.endpoint import endpoint_data

class SearchDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idsp', '2020-07-10', 'SearchData','idsp')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EntityName(self):
		return self.get_body_params().get('EntityName')

	def set_EntityName(self,EntityName):
		self.add_body_params('EntityName', EntityName)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_CurrentPage(self):
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_body_params('CurrentPage', CurrentPage)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_PosKeywords(self):
		return self.get_body_params().get('PosKeywords')

	def set_PosKeywords(self,PosKeywords):
		self.add_body_params('PosKeywords', PosKeywords)

	def get_TitleIncludeWords(self):
		return self.get_body_params().get('TitleIncludeWords')

	def set_TitleIncludeWords(self,TitleIncludeWords):
		self.add_body_params('TitleIncludeWords', TitleIncludeWords)

	def get_ExcludeKeywords(self):
		return self.get_body_params().get('ExcludeKeywords')

	def set_ExcludeKeywords(self,ExcludeKeywords):
		self.add_body_params('ExcludeKeywords', ExcludeKeywords)

	def get_SubjectId(self):
		return self.get_body_params().get('SubjectId')

	def set_SubjectId(self,SubjectId):
		self.add_body_params('SubjectId', SubjectId)

	def get_ParentId(self):
		return self.get_body_params().get('ParentId')

	def set_ParentId(self,ParentId):
		self.add_body_params('ParentId', ParentId)

	def get_PublishTimeEnd(self):
		return self.get_body_params().get('PublishTimeEnd')

	def set_PublishTimeEnd(self,PublishTimeEnd):
		self.add_body_params('PublishTimeEnd', PublishTimeEnd)

	def get_MediaTypeFilter(self):
		return self.get_body_params().get('MediaTypeFilter')

	def set_MediaTypeFilter(self,MediaTypeFilter):
		self.add_body_params('MediaTypeFilter', MediaTypeFilter)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_PublishTimeStart(self):
		return self.get_body_params().get('PublishTimeStart')

	def set_PublishTimeStart(self,PublishTimeStart):
		self.add_body_params('PublishTimeStart', PublishTimeStart)

	def get_AssKeywords(self):
		return self.get_body_params().get('AssKeywords')

	def set_AssKeywords(self,AssKeywords):
		self.add_body_params('AssKeywords', AssKeywords)