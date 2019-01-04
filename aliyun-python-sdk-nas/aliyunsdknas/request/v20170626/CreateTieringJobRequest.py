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
class CreateTieringJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateTieringJob','nas')

	def get_Volume(self):
		return self.get_query_params().get('Volume')

	def set_Volume(self,Volume):
		self.add_query_param('Volume',Volume)

	def get_Path(self):
		return self.get_query_params().get('Path')

	def set_Path(self,Path):
		self.add_query_param('Path',Path)

	def get_Hour(self):
		return self.get_query_params().get('Hour')

	def set_Hour(self,Hour):
		self.add_query_param('Hour',Hour)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Weekday(self):
		return self.get_query_params().get('Weekday')

	def set_Weekday(self,Weekday):
		self.add_query_param('Weekday',Weekday)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Recursive(self):
		return self.get_query_params().get('Recursive')

	def set_Recursive(self,Recursive):
		self.add_query_param('Recursive',Recursive)

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)