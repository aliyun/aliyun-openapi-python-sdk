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
class ImageDetectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2016-12-16', 'ImageDetection','green')
		self.set_method('POST')

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)

	def get_Async(self):
		return self.get_query_params().get('Async')

	def set_Async(self,Async):
		self.add_query_param('Async',Async)

	def get_NotifyUrl(self):
		return self.get_query_params().get('NotifyUrl')

	def set_NotifyUrl(self,NotifyUrl):
		self.add_query_param('NotifyUrl',NotifyUrl)

	def get_NotifySeed(self):
		return self.get_query_params().get('NotifySeed')

	def set_NotifySeed(self,NotifySeed):
		self.add_query_param('NotifySeed',NotifySeed)