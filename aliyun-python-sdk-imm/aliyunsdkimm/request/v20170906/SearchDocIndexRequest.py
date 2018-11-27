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
class SearchDocIndexRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'SearchDocIndex','imm')

	def get_ModifiedTimeEnd(self):
		return self.get_query_params().get('ModifiedTimeEnd')

	def set_ModifiedTimeEnd(self,ModifiedTimeEnd):
		self.add_query_param('ModifiedTimeEnd',ModifiedTimeEnd)

	def get_CustomKey1(self):
		return self.get_query_params().get('CustomKey1')

	def set_CustomKey1(self,CustomKey1):
		self.add_query_param('CustomKey1',CustomKey1)

	def get_Set(self):
		return self.get_query_params().get('Set')

	def set_Set(self,Set):
		self.add_query_param('Set',Set)

	def get_SizeLimitEnd(self):
		return self.get_query_params().get('SizeLimitEnd')

	def set_SizeLimitEnd(self,SizeLimitEnd):
		self.add_query_param('SizeLimitEnd',SizeLimitEnd)

	def get_CustomKey5(self):
		return self.get_query_params().get('CustomKey5')

	def set_CustomKey5(self,CustomKey5):
		self.add_query_param('CustomKey5',CustomKey5)

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_CustomKey4(self):
		return self.get_query_params().get('CustomKey4')

	def set_CustomKey4(self,CustomKey4):
		self.add_query_param('CustomKey4',CustomKey4)

	def get_CustomKey3(self):
		return self.get_query_params().get('CustomKey3')

	def set_CustomKey3(self,CustomKey3):
		self.add_query_param('CustomKey3',CustomKey3)

	def get_CustomKey2(self):
		return self.get_query_params().get('CustomKey2')

	def set_CustomKey2(self,CustomKey2):
		self.add_query_param('CustomKey2',CustomKey2)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_ModifiedTimeStart(self):
		return self.get_query_params().get('ModifiedTimeStart')

	def set_ModifiedTimeStart(self,ModifiedTimeStart):
		self.add_query_param('ModifiedTimeStart',ModifiedTimeStart)

	def get_PageNumLimitStart(self):
		return self.get_query_params().get('PageNumLimitStart')

	def set_PageNumLimitStart(self,PageNumLimitStart):
		self.add_query_param('PageNumLimitStart',PageNumLimitStart)

	def get_CustomKey6(self):
		return self.get_query_params().get('CustomKey6')

	def set_CustomKey6(self,CustomKey6):
		self.add_query_param('CustomKey6',CustomKey6)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)

	def get_PageNumLimitEnd(self):
		return self.get_query_params().get('PageNumLimitEnd')

	def set_PageNumLimitEnd(self,PageNumLimitEnd):
		self.add_query_param('PageNumLimitEnd',PageNumLimitEnd)

	def get_ContentType(self):
		return self.get_query_params().get('ContentType')

	def set_ContentType(self,ContentType):
		self.add_query_param('ContentType',ContentType)

	def get_SizeLimitStart(self):
		return self.get_query_params().get('SizeLimitStart')

	def set_SizeLimitStart(self,SizeLimitStart):
		self.add_query_param('SizeLimitStart',SizeLimitStart)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)