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
class UploadCustomIDImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'UploadCustomIDImage','finmall')
		self.set_method('POST')

	def get_ImageType(self):
		return self.get_body_params().get('ImageType')

	def set_ImageType(self,ImageType):
		self.add_body_params('ImageType', ImageType)

	def get_Side(self):
		return self.get_body_params().get('Side')

	def set_Side(self,Side):
		self.add_body_params('Side', Side)

	def get_ImageFile(self):
		return self.get_body_params().get('ImageFile')

	def set_ImageFile(self,ImageFile):
		self.add_body_params('ImageFile', ImageFile)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)