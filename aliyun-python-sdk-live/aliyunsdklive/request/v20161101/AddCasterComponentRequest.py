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
class AddCasterComponentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddCasterComponent','live')

	def get_ComponentType(self):
		return self.get_query_params().get('ComponentType')

	def set_ComponentType(self,ComponentType):
		self.add_query_param('ComponentType',ComponentType)

	def get_LocationId(self):
		return self.get_query_params().get('LocationId')

	def set_LocationId(self,LocationId):
		self.add_query_param('LocationId',LocationId)

	def get_ImageLayerContent(self):
		return self.get_query_params().get('ImageLayerContent')

	def set_ImageLayerContent(self,ImageLayerContent):
		self.add_query_param('ImageLayerContent',ImageLayerContent)

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_Effect(self):
		return self.get_query_params().get('Effect')

	def set_Effect(self,Effect):
		self.add_query_param('Effect',Effect)

	def get_ComponentLayer(self):
		return self.get_query_params().get('ComponentLayer')

	def set_ComponentLayer(self,ComponentLayer):
		self.add_query_param('ComponentLayer',ComponentLayer)

	def get_CaptionLayerContent(self):
		return self.get_query_params().get('CaptionLayerContent')

	def set_CaptionLayerContent(self,CaptionLayerContent):
		self.add_query_param('CaptionLayerContent',CaptionLayerContent)

	def get_ComponentName(self):
		return self.get_query_params().get('ComponentName')

	def set_ComponentName(self,ComponentName):
		self.add_query_param('ComponentName',ComponentName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TextLayerContent(self):
		return self.get_query_params().get('TextLayerContent')

	def set_TextLayerContent(self,TextLayerContent):
		self.add_query_param('TextLayerContent',TextLayerContent)