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
class RevertRpcRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2015-08-27', 'RevertRpc')

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_DeviceId(self):
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self,DeviceId):
		self.add_query_param('DeviceId',DeviceId)

	def get_RpcContent(self):
		return self.get_query_params().get('RpcContent')

	def set_RpcContent(self,RpcContent):
		self.add_query_param('RpcContent',RpcContent)

	def get_TimeOut(self):
		return self.get_query_params().get('TimeOut')

	def set_TimeOut(self,TimeOut):
		self.add_query_param('TimeOut',TimeOut)