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
class GenerateIotDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2015-08-27', 'GenerateIotDevices')

	def get_isDev(self):
		return self.get_query_params().get('isDev')

	def set_isDev(self,isDev):
		self.add_query_param('isDev',isDev)

	def get_Number(self):
		return self.get_query_params().get('Number')

	def set_Number(self,Number):
		self.add_query_param('Number',Number)