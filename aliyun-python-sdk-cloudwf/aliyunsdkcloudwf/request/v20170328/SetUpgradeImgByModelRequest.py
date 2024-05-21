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
class SetUpgradeImgByModelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SetUpgradeImgByModel','cloudwf')

	def get_ImgAddr(self):
		return self.get_query_params().get('ImgAddr')

	def set_ImgAddr(self,ImgAddr):
		self.add_query_param('ImgAddr',ImgAddr)

	def get_ImgVersion(self):
		return self.get_query_params().get('ImgVersion')

	def set_ImgVersion(self,ImgVersion):
		self.add_query_param('ImgVersion',ImgVersion)

	def get_ApModelId(self):
		return self.get_query_params().get('ApModelId')

	def set_ApModelId(self,ApModelId):
		self.add_query_param('ApModelId',ApModelId)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)