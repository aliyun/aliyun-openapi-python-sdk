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

class ModifyImageSharePermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ModifyImageSharePermission','ens')
		self.set_method('POST')

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_RemoveAccounts(self): # String
		return self.get_query_params().get('RemoveAccounts')

	def set_RemoveAccounts(self, RemoveAccounts):  # String
		self.add_query_param('RemoveAccounts', RemoveAccounts)
	def get_AddAccounts(self): # String
		return self.get_query_params().get('AddAccounts')

	def set_AddAccounts(self, AddAccounts):  # String
		self.add_query_param('AddAccounts', AddAccounts)
