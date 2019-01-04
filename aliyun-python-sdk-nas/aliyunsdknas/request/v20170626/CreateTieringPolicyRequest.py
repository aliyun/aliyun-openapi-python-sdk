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
class CreateTieringPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateTieringPolicy','nas')

	def get_Atime(self):
		return self.get_query_params().get('Atime')

	def set_Atime(self,Atime):
		self.add_query_param('Atime',Atime)

	def get_FileName(self):
		return self.get_query_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_query_param('FileName',FileName)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_RecallTime(self):
		return self.get_query_params().get('RecallTime')

	def set_RecallTime(self,RecallTime):
		self.add_query_param('RecallTime',RecallTime)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Ctime(self):
		return self.get_query_params().get('Ctime')

	def set_Ctime(self,Ctime):
		self.add_query_param('Ctime',Ctime)

	def get_Mtime(self):
		return self.get_query_params().get('Mtime')

	def set_Mtime(self,Mtime):
		self.add_query_param('Mtime',Mtime)

	def get_CheckLimit(self):
		return self.get_query_params().get('CheckLimit')

	def set_CheckLimit(self,CheckLimit):
		self.add_query_param('CheckLimit',CheckLimit)