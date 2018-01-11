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
class EditPhotoStoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'EditPhotoStore','cloudphoto')
		self.set_protocol_type('https');

	def get_AutoCleanEnabled(self):
		return self.get_query_params().get('AutoCleanEnabled')

	def set_AutoCleanEnabled(self,AutoCleanEnabled):
		self.add_query_param('AutoCleanEnabled',AutoCleanEnabled)

	def get_DefaultTrashQuota(self):
		return self.get_query_params().get('DefaultTrashQuota')

	def set_DefaultTrashQuota(self,DefaultTrashQuota):
		self.add_query_param('DefaultTrashQuota',DefaultTrashQuota)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_DefaultQuota(self):
		return self.get_query_params().get('DefaultQuota')

	def set_DefaultQuota(self,DefaultQuota):
		self.add_query_param('DefaultQuota',DefaultQuota)

	def get_AutoCleanDays(self):
		return self.get_query_params().get('AutoCleanDays')

	def set_AutoCleanDays(self,AutoCleanDays):
		self.add_query_param('AutoCleanDays',AutoCleanDays)