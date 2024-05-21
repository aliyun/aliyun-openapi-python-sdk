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
class SetAllowIPRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'openanalytics', '2018-03-01', 'SetAllowIP','openanalytics')

	def get_UserID(self):
		return self.get_body_params().get('UserID')

	def set_UserID(self,UserID):
		self.add_body_params('UserID', UserID)

	def get_NetworkType(self):
		return self.get_body_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_body_params('NetworkType', NetworkType)

	def get_AllowIP(self):
		return self.get_body_params().get('AllowIP')

	def set_AllowIP(self,AllowIP):
		self.add_body_params('AllowIP', AllowIP)

	def get_Append(self):
		return self.get_body_params().get('Append')

	def set_Append(self,Append):
		self.add_body_params('Append', Append)