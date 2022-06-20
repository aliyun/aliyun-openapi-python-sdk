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

class DescribeUuidsByVulNamesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeUuidsByVulNames')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StatusList(self): # String
		return self.get_query_params().get('StatusList')

	def set_StatusList(self, StatusList):  # String
		self.add_query_param('StatusList', StatusList)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_VpcInstanceIds(self): # String
		return self.get_query_params().get('VpcInstanceIds')

	def set_VpcInstanceIds(self, VpcInstanceIds):  # String
		self.add_query_param('VpcInstanceIds', VpcInstanceIds)
	def get_VulNamess(self): # RepeatList
		return self.get_query_params().get('VulNames')

	def set_VulNamess(self, VulNames):  # RepeatList
		for depth1 in range(len(VulNames)):
			self.add_query_param('VulNames.' + str(depth1 + 1), VulNames[depth1])
	def get_Tag(self): # String
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_query_param('Tag', Tag)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Level(self): # String
		return self.get_query_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_query_param('Level', Level)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_Dealed(self): # String
		return self.get_query_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_query_param('Dealed', Dealed)
	def get_FieldValue(self): # String
		return self.get_query_params().get('FieldValue')

	def set_FieldValue(self, FieldValue):  # String
		self.add_query_param('FieldValue', FieldValue)
	def get_FieldName(self): # String
		return self.get_query_params().get('FieldName')

	def set_FieldName(self, FieldName):  # String
		self.add_query_param('FieldName', FieldName)
	def get_SearchTags(self): # String
		return self.get_query_params().get('SearchTags')

	def set_SearchTags(self, SearchTags):  # String
		self.add_query_param('SearchTags', SearchTags)
	def get_Necessity(self): # String
		return self.get_query_params().get('Necessity')

	def set_Necessity(self, Necessity):  # String
		self.add_query_param('Necessity', Necessity)
