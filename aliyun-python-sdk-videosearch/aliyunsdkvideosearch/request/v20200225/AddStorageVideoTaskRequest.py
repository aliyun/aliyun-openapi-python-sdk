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

class AddStorageVideoTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videosearch', '2020-02-25', 'AddStorageVideoTask')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_VideoTags(self):
		return self.get_body_params().get('VideoTags')

	def set_VideoTags(self,VideoTags):
		self.add_body_params('VideoTags', VideoTags)

	def get_VideoId(self):
		return self.get_body_params().get('VideoId')

	def set_VideoId(self,VideoId):
		self.add_body_params('VideoId', VideoId)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_VideoUrl(self):
		return self.get_body_params().get('VideoUrl')

	def set_VideoUrl(self,VideoUrl):
		self.add_body_params('VideoUrl', VideoUrl)

	def get_CallbackUrl(self):
		return self.get_body_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_body_params('CallbackUrl', CallbackUrl)