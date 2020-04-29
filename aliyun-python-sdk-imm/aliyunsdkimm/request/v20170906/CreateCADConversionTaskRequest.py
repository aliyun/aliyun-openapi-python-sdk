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

class CreateCADConversionTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'CreateCADConversionTask','imm')
		self.set_method('POST')

	def get_SrcType(self):
		return self.get_query_params().get('SrcType')

	def set_SrcType(self,SrcType):
		self.add_query_param('SrcType',SrcType)

	def get_BaseRow(self):
		return self.get_query_params().get('BaseRow')

	def set_BaseRow(self,BaseRow):
		self.add_query_param('BaseRow',BaseRow)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_ZoomFactor(self):
		return self.get_query_params().get('ZoomFactor')

	def set_ZoomFactor(self,ZoomFactor):
		self.add_query_param('ZoomFactor',ZoomFactor)

	def get_NotifyEndpoint(self):
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self,NotifyEndpoint):
		self.add_query_param('NotifyEndpoint',NotifyEndpoint)

	def get_BaseCol(self):
		return self.get_query_params().get('BaseCol')

	def set_BaseCol(self,BaseCol):
		self.add_query_param('BaseCol',BaseCol)

	def get_NotifyTopicName(self):
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self,NotifyTopicName):
		self.add_query_param('NotifyTopicName',NotifyTopicName)

	def get_UnitWidth(self):
		return self.get_query_params().get('UnitWidth')

	def set_UnitWidth(self,UnitWidth):
		self.add_query_param('UnitWidth',UnitWidth)

	def get_ZoomLevel(self):
		return self.get_query_params().get('ZoomLevel')

	def set_ZoomLevel(self,ZoomLevel):
		self.add_query_param('ZoomLevel',ZoomLevel)

	def get_ModelId(self):
		return self.get_query_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_query_param('ModelId',ModelId)

	def get_TgtType(self):
		return self.get_query_params().get('TgtType')

	def set_TgtType(self,TgtType):
		self.add_query_param('TgtType',TgtType)

	def get_UnitHeight(self):
		return self.get_query_params().get('UnitHeight')

	def set_UnitHeight(self,UnitHeight):
		self.add_query_param('UnitHeight',UnitHeight)

	def get_SrcUri(self):
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self,SrcUri):
		self.add_query_param('SrcUri',SrcUri)

	def get_Thumbnails(self):
		return self.get_query_params().get('Thumbnails')

	def set_Thumbnails(self,Thumbnails):
		self.add_query_param('Thumbnails',Thumbnails)

	def get_TgtUri(self):
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self,TgtUri):
		self.add_query_param('TgtUri',TgtUri)