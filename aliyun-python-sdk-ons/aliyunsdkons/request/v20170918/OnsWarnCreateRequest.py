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
class OnsWarnCreateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ons', '2017-09-18', 'OnsWarnCreate')

	def get_PreventCache(self):
		return self.get_query_params().get('PreventCache')

	def set_PreventCache(self,PreventCache):
		self.add_query_param('PreventCache',PreventCache)

	def get_OnsRegionId(self):
		return self.get_query_params().get('OnsRegionId')

	def set_OnsRegionId(self,OnsRegionId):
		self.add_query_param('OnsRegionId',OnsRegionId)

	def get_OnsPlatform(self):
		return self.get_query_params().get('OnsPlatform')

	def set_OnsPlatform(self,OnsPlatform):
		self.add_query_param('OnsPlatform',OnsPlatform)

	def get_BlockTime(self):
		return self.get_query_params().get('BlockTime')

	def set_BlockTime(self,BlockTime):
		self.add_query_param('BlockTime',BlockTime)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_ConsumerId(self):
		return self.get_query_params().get('ConsumerId')

	def set_ConsumerId(self,ConsumerId):
		self.add_query_param('ConsumerId',ConsumerId)

	def get_DelayTime(self):
		return self.get_query_params().get('DelayTime')

	def set_DelayTime(self,DelayTime):
		self.add_query_param('DelayTime',DelayTime)

	def get_Topic(self):
		return self.get_query_params().get('Topic')

	def set_Topic(self,Topic):
		self.add_query_param('Topic',Topic)

	def get_Threshold(self):
		return self.get_query_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_query_param('Threshold',Threshold)

	def get_AlertTime(self):
		return self.get_query_params().get('AlertTime')

	def set_AlertTime(self,AlertTime):
		self.add_query_param('AlertTime',AlertTime)

	def get_Contacts(self):
		return self.get_query_params().get('Contacts')

	def set_Contacts(self,Contacts):
		self.add_query_param('Contacts',Contacts)