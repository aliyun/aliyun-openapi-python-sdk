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

class DefineTagRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudmarketing', '2018-09-10', 'DefineTag')
		self.set_method('POST')

	def get_OptionType(self):
		return self.get_body_params().get('OptionType')

	def set_OptionType(self,OptionType):
		self.add_body_params('OptionType', OptionType)

	def get_ValidTime(self):
		return self.get_body_params().get('ValidTime')

	def set_ValidTime(self,ValidTime):
		self.add_body_params('ValidTime', ValidTime)

	def get_OptionDefiness(self):
		return self.get_body_params().get('OptionDefiness')

	def set_OptionDefiness(self, OptionDefiness):
		for depth1 in range(len(OptionDefiness)):
			if OptionDefiness[depth1].get('Name') is not None:
				self.add_body_params('OptionDefines.' + str(depth1 + 1) + '.Name', OptionDefiness[depth1].get('Name'))
			if OptionDefiness[depth1].get('Define') is not None:
				self.add_body_params('OptionDefines.' + str(depth1 + 1) + '.Define', OptionDefiness[depth1].get('Define'))
			if OptionDefiness[depth1].get('Value') is not None:
				self.add_body_params('OptionDefines.' + str(depth1 + 1) + '.Value', OptionDefiness[depth1].get('Value'))

	def get_TagName(self):
		return self.get_body_params().get('TagName')

	def set_TagName(self,TagName):
		self.add_body_params('TagName', TagName)

	def get_ColumnIndex(self):
		return self.get_body_params().get('ColumnIndex')

	def set_ColumnIndex(self,ColumnIndex):
		self.add_body_params('ColumnIndex', ColumnIndex)

	def get_TagDesc(self):
		return self.get_body_params().get('TagDesc')

	def set_TagDesc(self,TagDesc):
		self.add_body_params('TagDesc', TagDesc)

	def get_CategoryId(self):
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_body_params('CategoryId', CategoryId)

	def get_FileId(self):
		return self.get_body_params().get('FileId')

	def set_FileId(self,FileId):
		self.add_body_params('FileId', FileId)