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
class OnsMqttQueryMsgTransTrendRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ons', '2017-09-18', 'OnsMqttQueryMsgTransTrend')

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

	def get_Qos(self):
		return self.get_query_params().get('Qos')

	def set_Qos(self,Qos):
		self.add_query_param('Qos',Qos)

	def get_TransType(self):
		return self.get_query_params().get('TransType')

	def set_TransType(self,TransType):
		self.add_query_param('TransType',TransType)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_BeginTime(self):
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self,BeginTime):
		self.add_query_param('BeginTime',BeginTime)

	def get_TpsType(self):
		return self.get_query_params().get('TpsType')

	def set_TpsType(self,TpsType):
		self.add_query_param('TpsType',TpsType)

	def get_ParentTopic(self):
		return self.get_query_params().get('ParentTopic')

	def set_ParentTopic(self,ParentTopic):
		self.add_query_param('ParentTopic',ParentTopic)

	def get_MsgType(self):
		return self.get_query_params().get('MsgType')

	def set_MsgType(self,MsgType):
		self.add_query_param('MsgType',MsgType)

	def get_SubTopic(self):
		return self.get_query_params().get('SubTopic')

	def set_SubTopic(self,SubTopic):
		self.add_query_param('SubTopic',SubTopic)