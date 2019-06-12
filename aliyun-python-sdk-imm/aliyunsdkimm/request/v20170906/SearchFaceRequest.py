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
class SearchFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'SearchFace','imm')

	def get_ResultNum(self):
		return self.get_query_params().get('ResultNum')

	def set_ResultNum(self,ResultNum):
		self.add_query_param('ResultNum',ResultNum)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_SearchThresholdLevel(self):
		return self.get_query_params().get('SearchThresholdLevel')

	def set_SearchThresholdLevel(self,SearchThresholdLevel):
		self.add_query_param('SearchThresholdLevel',SearchThresholdLevel)

	def get_SrcUri(self):
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self,SrcUri):
		self.add_query_param('SrcUri',SrcUri)

	def get_IsThreshold(self):
		return self.get_query_params().get('IsThreshold')

	def set_IsThreshold(self,IsThreshold):
		self.add_query_param('IsThreshold',IsThreshold)

	def get_GroupName(self):
		return self.get_query_params().get('GroupName')

	def set_GroupName(self,GroupName):
		self.add_query_param('GroupName',GroupName)