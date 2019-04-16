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
class DeleteImageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ImageSearch', '2019-03-25', 'DeleteImage','imagesearch')
		self.set_uri_pattern('/v2/image/delete')
		self.set_method('POST')

	def get_InstanceName(self):
		return self.get_body_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_body_params('InstanceName', InstanceName)

	def get_ProductId(self):
		return self.get_body_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_body_params('ProductId', ProductId)

	def get_PicName(self):
		return self.get_body_params().get('PicName')

	def set_PicName(self,PicName):
		self.add_body_params('PicName', PicName)