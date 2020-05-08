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

class ChangeInstanceNetworkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'ChangeInstanceNetwork','drds')

	def get_VswitchId(self):
		return self.get_query_params().get('VswitchId')

	def set_VswitchId(self,VswitchId):
		self.add_query_param('VswitchId',VswitchId)

	def get_RetainClassic(self):
		return self.get_query_params().get('RetainClassic')

	def set_RetainClassic(self,RetainClassic):
		self.add_query_param('RetainClassic',RetainClassic)

	def get_ClassicExpiredDays(self):
		return self.get_query_params().get('ClassicExpiredDays')

	def set_ClassicExpiredDays(self,ClassicExpiredDays):
		self.add_query_param('ClassicExpiredDays',ClassicExpiredDays)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_SrcInstanceNetworkType(self):
		return self.get_query_params().get('SrcInstanceNetworkType')

	def set_SrcInstanceNetworkType(self,SrcInstanceNetworkType):
		self.add_query_param('SrcInstanceNetworkType',SrcInstanceNetworkType)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)