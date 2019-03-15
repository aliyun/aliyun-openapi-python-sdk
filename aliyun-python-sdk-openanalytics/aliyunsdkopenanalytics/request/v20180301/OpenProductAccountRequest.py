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
class OpenProductAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'openanalytics', '2018-03-01', 'OpenProductAccount','openanalytics')

	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_ProductAccessKey(self):
		return self.get_body_params().get('ProductAccessKey')

	def set_ProductAccessKey(self,ProductAccessKey):
		self.add_body_params('ProductAccessKey', ProductAccessKey)

	def get_TargetUid(self):
		return self.get_body_params().get('TargetUid')

	def set_TargetUid(self,TargetUid):
		self.add_body_params('TargetUid', TargetUid)

	def get_TargetArnRole(self):
		return self.get_body_params().get('TargetArnRole')

	def set_TargetArnRole(self,TargetArnRole):
		self.add_body_params('TargetArnRole', TargetArnRole)