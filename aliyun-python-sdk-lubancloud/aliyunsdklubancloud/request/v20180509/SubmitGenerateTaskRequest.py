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
class SubmitGenerateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lubancloud', '2018-05-09', 'SubmitGenerateTask','luban')
		self.set_method('POST')

	def get_ImageCount(self):
		return self.get_query_params().get('ImageCount')

	def set_ImageCount(self,ImageCount):
		self.add_query_param('ImageCount',ImageCount)

	def get_ActionPoint(self):
		return self.get_query_params().get('ActionPoint')

	def set_ActionPoint(self,ActionPoint):
		self.add_query_param('ActionPoint',ActionPoint)

	def get_LogoImagePath(self):
		return self.get_query_params().get('LogoImagePath')

	def set_LogoImagePath(self,LogoImagePath):
		self.add_query_param('LogoImagePath',LogoImagePath)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_MajorImagePaths(self):
		return self.get_query_params().get('MajorImagePaths')

	def set_MajorImagePaths(self,MajorImagePaths):
		for i in range(len(MajorImagePaths)):	
			if MajorImagePaths[i] is not None:
				self.add_query_param('MajorImagePath.' + str(i + 1) , MajorImagePaths[i]);

	def get_Width(self):
		return self.get_query_params().get('Width')

	def set_Width(self,Width):
		self.add_query_param('Width',Width)

	def get_CopyWrites(self):
		return self.get_query_params().get('CopyWrites')

	def set_CopyWrites(self,CopyWrites):
		for i in range(len(CopyWrites)):	
			if CopyWrites[i] is not None:
				self.add_query_param('CopyWrite.' + str(i + 1) , CopyWrites[i]);

	def get_PropertyIds(self):
		return self.get_query_params().get('PropertyIds')

	def set_PropertyIds(self,PropertyIds):
		for i in range(len(PropertyIds)):	
			if PropertyIds[i] is not None:
				self.add_query_param('PropertyId.' + str(i + 1) , PropertyIds[i]);

	def get_Height(self):
		return self.get_query_params().get('Height')

	def set_Height(self,Height):
		self.add_query_param('Height',Height)