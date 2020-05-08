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

class GetOfficePreviewURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'GetOfficePreviewURL','imm')
		self.set_method('POST')

	def get_SrcType(self):
		return self.get_query_params().get('SrcType')

	def set_SrcType(self,SrcType):
		self.add_query_param('SrcType',SrcType)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_WatermarkVertical(self):
		return self.get_query_params().get('WatermarkVertical')

	def set_WatermarkVertical(self,WatermarkVertical):
		self.add_query_param('WatermarkVertical',WatermarkVertical)

	def get_WatermarkType(self):
		return self.get_query_params().get('WatermarkType')

	def set_WatermarkType(self,WatermarkType):
		self.add_query_param('WatermarkType',WatermarkType)

	def get_WatermarkRotate(self):
		return self.get_query_params().get('WatermarkRotate')

	def set_WatermarkRotate(self,WatermarkRotate):
		self.add_query_param('WatermarkRotate',WatermarkRotate)

	def get_WatermarkValue(self):
		return self.get_query_params().get('WatermarkValue')

	def set_WatermarkValue(self,WatermarkValue):
		self.add_query_param('WatermarkValue',WatermarkValue)

	def get_WatermarkFont(self):
		return self.get_query_params().get('WatermarkFont')

	def set_WatermarkFont(self,WatermarkFont):
		self.add_query_param('WatermarkFont',WatermarkFont)

	def get_WatermarkHorizontal(self):
		return self.get_query_params().get('WatermarkHorizontal')

	def set_WatermarkHorizontal(self,WatermarkHorizontal):
		self.add_query_param('WatermarkHorizontal',WatermarkHorizontal)

	def get_SrcUri(self):
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self,SrcUri):
		self.add_query_param('SrcUri',SrcUri)

	def get_WatermarkFillStyle(self):
		return self.get_query_params().get('WatermarkFillStyle')

	def set_WatermarkFillStyle(self,WatermarkFillStyle):
		self.add_query_param('WatermarkFillStyle',WatermarkFillStyle)