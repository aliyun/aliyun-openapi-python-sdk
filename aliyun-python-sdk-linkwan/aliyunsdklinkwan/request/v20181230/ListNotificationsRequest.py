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
class ListNotificationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'ListNotifications','linkwan')
		self.set_protocol_type('https');

	def get_Offset(self):
		return self.get_body_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_body_params('Offset', Offset)

	def get_EndMillis(self):
		return self.get_body_params().get('EndMillis')

	def set_EndMillis(self,EndMillis):
		self.add_body_params('EndMillis', EndMillis)

	def get_HandleState(self):
		return self.get_body_params().get('HandleState')

	def set_HandleState(self,HandleState):
		self.add_body_params('HandleState', HandleState)

	def get_Limit(self):
		return self.get_body_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_body_params('Limit', Limit)

	def get_Categorys(self):
		return self.get_body_params().get('Categorys')

	def set_Categorys(self,Categorys):
		for i in range(len(Categorys)):	
			if Categorys[i] is not None:
				self.add_body_params('Category.' + str(i + 1) , Categorys[i]);

	def get_BeginMillis(self):
		return self.get_body_params().get('BeginMillis')

	def set_BeginMillis(self,BeginMillis):
		self.add_body_params('BeginMillis', BeginMillis)

	def get_SortingField(self):
		return self.get_body_params().get('SortingField')

	def set_SortingField(self,SortingField):
		self.add_body_params('SortingField', SortingField)

	def get_Ascending(self):
		return self.get_body_params().get('Ascending')

	def set_Ascending(self,Ascending):
		self.add_body_params('Ascending', Ascending)