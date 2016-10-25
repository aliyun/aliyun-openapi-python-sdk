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
class PushRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2015-08-27', 'Push')

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_TargetValue(self):
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self,TargetValue):
		self.add_query_param('TargetValue',TargetValue)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_Body(self):
		return self.get_query_params().get('Body')

	def set_Body(self,Body):
		self.add_query_param('Body',Body)

	def get_Summary(self):
		return self.get_query_params().get('Summary')

	def set_Summary(self,Summary):
		self.add_query_param('Summary',Summary)

	def get_TimeOut(self):
		return self.get_query_params().get('TimeOut')

	def set_TimeOut(self,TimeOut):
		self.add_query_param('TimeOut',TimeOut)

	def get_Remind(self):
		return self.get_query_params().get('Remind')

	def set_Remind(self,Remind):
		self.add_query_param('Remind',Remind)

	def get_StoreOffline(self):
		return self.get_query_params().get('StoreOffline')

	def set_StoreOffline(self,StoreOffline):
		self.add_query_param('StoreOffline',StoreOffline)

	def get_AndroidActivity(self):
		return self.get_query_params().get('AndroidActivity')

	def set_AndroidActivity(self,AndroidActivity):
		self.add_query_param('AndroidActivity',AndroidActivity)

	def get_XiaomiActivity(self):
		return self.get_query_params().get('XiaomiActivity')

	def set_XiaomiActivity(self,XiaomiActivity):
		self.add_query_param('XiaomiActivity',XiaomiActivity)

	def get_AndroidOpenUrl(self):
		return self.get_query_params().get('AndroidOpenUrl')

	def set_AndroidOpenUrl(self,AndroidOpenUrl):
		self.add_query_param('AndroidOpenUrl',AndroidOpenUrl)

	def get_AndroidExtParameters(self):
		return self.get_query_params().get('AndroidExtParameters')

	def set_AndroidExtParameters(self,AndroidExtParameters):
		self.add_query_param('AndroidExtParameters',AndroidExtParameters)

	def get_AndroidOpenType(self):
		return self.get_query_params().get('AndroidOpenType')

	def set_AndroidOpenType(self,AndroidOpenType):
		self.add_query_param('AndroidOpenType',AndroidOpenType)

	def get_AndroidMusic(self):
		return self.get_query_params().get('AndroidMusic')

	def set_AndroidMusic(self,AndroidMusic):
		self.add_query_param('AndroidMusic',AndroidMusic)

	def get_BatchNumber(self):
		return self.get_query_params().get('BatchNumber')

	def set_BatchNumber(self,BatchNumber):
		self.add_query_param('BatchNumber',BatchNumber)

	def get_iOSMusic(self):
		return self.get_query_params().get('iOSMusic')

	def set_iOSMusic(self,iOSMusic):
		self.add_query_param('iOSMusic',iOSMusic)

	def get_iOSBadge(self):
		return self.get_query_params().get('iOSBadge')

	def set_iOSBadge(self,iOSBadge):
		self.add_query_param('iOSBadge',iOSBadge)

	def get_iOSTitle(self):
		return self.get_query_params().get('iOSTitle')

	def set_iOSTitle(self,iOSTitle):
		self.add_query_param('iOSTitle',iOSTitle)

	def get_iOSSubtitle(self):
		return self.get_query_params().get('iOSSubtitle')

	def set_iOSSubtitle(self,iOSSubtitle):
		self.add_query_param('iOSSubtitle',iOSSubtitle)

	def get_iOSNotificationCategory(self):
		return self.get_query_params().get('iOSNotificationCategory')

	def set_iOSNotificationCategory(self,iOSNotificationCategory):
		self.add_query_param('iOSNotificationCategory',iOSNotificationCategory)

	def get_iOSMutableContent(self):
		return self.get_query_params().get('iOSMutableContent')

	def set_iOSMutableContent(self,iOSMutableContent):
		self.add_query_param('iOSMutableContent',iOSMutableContent)

	def get_iOSExtParameters(self):
		return self.get_query_params().get('iOSExtParameters')

	def set_iOSExtParameters(self,iOSExtParameters):
		self.add_query_param('iOSExtParameters',iOSExtParameters)

	def get_PushTime(self):
		return self.get_query_params().get('PushTime')

	def set_PushTime(self,PushTime):
		self.add_query_param('PushTime',PushTime)

	def get_ApnsEnv(self):
		return self.get_query_params().get('ApnsEnv')

	def set_ApnsEnv(self,ApnsEnv):
		self.add_query_param('ApnsEnv',ApnsEnv)

	def get_ExpireTime(self):
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self,ExpireTime):
		self.add_query_param('ExpireTime',ExpireTime)