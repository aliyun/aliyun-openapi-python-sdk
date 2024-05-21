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

from aliyunsdkcore.request import RoaRequest
class AddImageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ImageSearch', '2019-03-25', 'AddImage','imagesearch')
		self.set_uri_pattern('/v2/image/add')
		self.set_method('POST')

	def get_PicContent(self):
		return self.get_body_params().get('PicContent')

	def set_PicContent(self,PicContent):
		self.add_body_params('PicContent', PicContent)

	def get_StrAttr(self):
		return self.get_body_params().get('StrAttr')

	def set_StrAttr(self,StrAttr):
		self.add_body_params('StrAttr', StrAttr)

	def get_InstanceName(self):
		return self.get_body_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_body_params('InstanceName', InstanceName)

	def get_IntAttr(self):
		return self.get_body_params().get('IntAttr')

	def set_IntAttr(self,IntAttr):
		self.add_body_params('IntAttr', IntAttr)

	def get_ProductId(self):
		return self.get_body_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_body_params('ProductId', ProductId)

	def get_PicName(self):
		return self.get_body_params().get('PicName')

	def set_PicName(self,PicName):
		self.add_body_params('PicName', PicName)

	def get_CustomContent(self):
		return self.get_body_params().get('CustomContent')

	def set_CustomContent(self,CustomContent):
		self.add_body_params('CustomContent', CustomContent)

	def get_Region(self):
		return self.get_body_params().get('Region')

	def set_Region(self,Region):
		self.add_body_params('Region', Region)

	def get_CategoryId(self):
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_body_params('CategoryId', CategoryId)

	def get_Crop(self):
		return self.get_body_params().get('Crop')

	def set_Crop(self,Crop):
		self.add_body_params('Crop', Crop)