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

class DescribeUuidsByVulNamesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeUuidsByVulNames','sas')
		self.set_method('POST')

	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_VpcInstanceIds(self):
		return self.get_query_params().get('VpcInstanceIds')

	def set_VpcInstanceIds(self,VpcInstanceIds):
		self.add_query_param('VpcInstanceIds',VpcInstanceIds)

	def get_VulNamess(self):
		return self.get_query_params().get('VulNames')

	def set_VulNamess(self, VulNamess):
		for depth1 in range(len(VulNamess)):
			if VulNamess[depth1] is not None:
				self.add_query_param('VulNames.' + str(depth1 + 1) , VulNamess[depth1])

	def get_Tag(self):
		return self.get_query_params().get('Tag')

	def set_Tag(self,Tag):
		self.add_query_param('Tag',Tag)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_FieldValue(self):
		return self.get_query_params().get('FieldValue')

	def set_FieldValue(self,FieldValue):
		self.add_query_param('FieldValue',FieldValue)

	def get_FieldName(self):
		return self.get_query_params().get('FieldName')

	def set_FieldName(self,FieldName):
		self.add_query_param('FieldName',FieldName)

	def get_SearchTags(self):
		return self.get_query_params().get('SearchTags')

	def set_SearchTags(self,SearchTags):
		self.add_query_param('SearchTags',SearchTags)

	def get_Necessity(self):
		return self.get_query_params().get('Necessity')

	def set_Necessity(self,Necessity):
		self.add_query_param('Necessity',Necessity)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)