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
class ShopDataAlarmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ShopDataAlarm','cloudwf')

	def get_WarnPhone(self):
		return self.get_query_params().get('WarnPhone')

	def set_WarnPhone(self,WarnPhone):
		self.add_query_param('WarnPhone',WarnPhone)

	def get_Warn(self):
		return self.get_query_params().get('Warn')

	def set_Warn(self,Warn):
		self.add_query_param('Warn',Warn)

	def get_CloseWarn(self):
		return self.get_query_params().get('CloseWarn')

	def set_CloseWarn(self,CloseWarn):
		self.add_query_param('CloseWarn',CloseWarn)

	def get_WarnEmail(self):
		return self.get_query_params().get('WarnEmail')

	def set_WarnEmail(self,WarnEmail):
		self.add_query_param('WarnEmail',WarnEmail)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)