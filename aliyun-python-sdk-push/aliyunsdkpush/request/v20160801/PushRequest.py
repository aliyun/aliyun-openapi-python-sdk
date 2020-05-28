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
from aliyunsdkpush.endpoint import endpoint_data

class PushRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'Push')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AndroidNotificationBarType(self):
		return self.get_query_params().get('AndroidNotificationBarType')

	def set_AndroidNotificationBarType(self,AndroidNotificationBarType):
		self.add_query_param('AndroidNotificationBarType',AndroidNotificationBarType)

	def get_SmsSendPolicy(self):
		return self.get_query_params().get('SmsSendPolicy')

	def set_SmsSendPolicy(self,SmsSendPolicy):
		self.add_query_param('SmsSendPolicy',SmsSendPolicy)

	def get_Body(self):
		return self.get_query_params().get('Body')

	def set_Body(self,Body):
		self.add_query_param('Body',Body)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_PushTime(self):
		return self.get_query_params().get('PushTime')

	def set_PushTime(self,PushTime):
		self.add_query_param('PushTime',PushTime)

	def get_SendSpeed(self):
		return self.get_query_params().get('SendSpeed')

	def set_SendSpeed(self,SendSpeed):
		self.add_query_param('SendSpeed',SendSpeed)

	def get_AndroidPopupActivity(self):
		return self.get_query_params().get('AndroidPopupActivity')

	def set_AndroidPopupActivity(self,AndroidPopupActivity):
		self.add_query_param('AndroidPopupActivity',AndroidPopupActivity)

	def get_iOSRemindBody(self):
		return self.get_query_params().get('iOSRemindBody')

	def set_iOSRemindBody(self,iOSRemindBody):
		self.add_query_param('iOSRemindBody',iOSRemindBody)

	def get_AndroidNotifyType(self):
		return self.get_query_params().get('AndroidNotifyType')

	def set_AndroidNotifyType(self,AndroidNotifyType):
		self.add_query_param('AndroidNotifyType',AndroidNotifyType)

	def get_AndroidPopupTitle(self):
		return self.get_query_params().get('AndroidPopupTitle')

	def set_AndroidPopupTitle(self,AndroidPopupTitle):
		self.add_query_param('AndroidPopupTitle',AndroidPopupTitle)

	def get_iOSMusic(self):
		return self.get_query_params().get('iOSMusic')

	def set_iOSMusic(self,iOSMusic):
		self.add_query_param('iOSMusic',iOSMusic)

	def get_iOSApnsEnv(self):
		return self.get_query_params().get('iOSApnsEnv')

	def set_iOSApnsEnv(self,iOSApnsEnv):
		self.add_query_param('iOSApnsEnv',iOSApnsEnv)

	def get_iOSMutableContent(self):
		return self.get_query_params().get('iOSMutableContent')

	def set_iOSMutableContent(self,iOSMutableContent):
		self.add_query_param('iOSMutableContent',iOSMutableContent)

	def get_AndroidNotificationBarPriority(self):
		return self.get_query_params().get('AndroidNotificationBarPriority')

	def set_AndroidNotificationBarPriority(self,AndroidNotificationBarPriority):
		self.add_query_param('AndroidNotificationBarPriority',AndroidNotificationBarPriority)

	def get_ExpireTime(self):
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self,ExpireTime):
		self.add_query_param('ExpireTime',ExpireTime)

	def get_iOSNotificationCategory(self):
		return self.get_query_params().get('iOSNotificationCategory')

	def set_iOSNotificationCategory(self,iOSNotificationCategory):
		self.add_query_param('iOSNotificationCategory',iOSNotificationCategory)

	def get_AndroidNotificationXiaomiChannel(self):
		return self.get_query_params().get('AndroidNotificationXiaomiChannel')

	def set_AndroidNotificationXiaomiChannel(self,AndroidNotificationXiaomiChannel):
		self.add_query_param('AndroidNotificationXiaomiChannel',AndroidNotificationXiaomiChannel)

	def get_StoreOffline(self):
		return self.get_query_params().get('StoreOffline')

	def set_StoreOffline(self,StoreOffline):
		self.add_query_param('StoreOffline',StoreOffline)

	def get_SmsParams(self):
		return self.get_query_params().get('SmsParams')

	def set_SmsParams(self,SmsParams):
		self.add_query_param('SmsParams',SmsParams)

	def get_JobKey(self):
		return self.get_query_params().get('JobKey')

	def set_JobKey(self,JobKey):
		self.add_query_param('JobKey',JobKey)

	def get_AndroidOpenUrl(self):
		return self.get_query_params().get('AndroidOpenUrl')

	def set_AndroidOpenUrl(self,AndroidOpenUrl):
		self.add_query_param('AndroidOpenUrl',AndroidOpenUrl)

	def get_AndroidXiaoMiNotifyBody(self):
		return self.get_query_params().get('AndroidXiaoMiNotifyBody')

	def set_AndroidXiaoMiNotifyBody(self,AndroidXiaoMiNotifyBody):
		self.add_query_param('AndroidXiaoMiNotifyBody',AndroidXiaoMiNotifyBody)

	def get_iOSSubtitle(self):
		return self.get_query_params().get('iOSSubtitle')

	def set_iOSSubtitle(self,iOSSubtitle):
		self.add_query_param('iOSSubtitle',iOSSubtitle)

	def get_iOSRemind(self):
		return self.get_query_params().get('iOSRemind')

	def set_iOSRemind(self,iOSRemind):
		self.add_query_param('iOSRemind',iOSRemind)

	def get_AndroidMusic(self):
		return self.get_query_params().get('AndroidMusic')

	def set_AndroidMusic(self,AndroidMusic):
		self.add_query_param('AndroidMusic',AndroidMusic)

	def get_PushType(self):
		return self.get_query_params().get('PushType')

	def set_PushType(self,PushType):
		self.add_query_param('PushType',PushType)

	def get_AndroidExtParameters(self):
		return self.get_query_params().get('AndroidExtParameters')

	def set_AndroidExtParameters(self,AndroidExtParameters):
		self.add_query_param('AndroidExtParameters',AndroidExtParameters)

	def get_iOSBadge(self):
		return self.get_query_params().get('iOSBadge')

	def set_iOSBadge(self,iOSBadge):
		self.add_query_param('iOSBadge',iOSBadge)

	def get_iOSBadgeAutoIncrement(self):
		return self.get_query_params().get('iOSBadgeAutoIncrement')

	def set_iOSBadgeAutoIncrement(self,iOSBadgeAutoIncrement):
		self.add_query_param('iOSBadgeAutoIncrement',iOSBadgeAutoIncrement)

	def get_AndroidOpenType(self):
		return self.get_query_params().get('AndroidOpenType')

	def set_AndroidOpenType(self,AndroidOpenType):
		self.add_query_param('AndroidOpenType',AndroidOpenType)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_SmsDelaySecs(self):
		return self.get_query_params().get('SmsDelaySecs')

	def set_SmsDelaySecs(self,SmsDelaySecs):
		self.add_query_param('SmsDelaySecs',SmsDelaySecs)

	def get_iOSExtParameters(self):
		return self.get_query_params().get('iOSExtParameters')

	def set_iOSExtParameters(self,iOSExtParameters):
		self.add_query_param('iOSExtParameters',iOSExtParameters)

	def get_SmsTemplateName(self):
		return self.get_query_params().get('SmsTemplateName')

	def set_SmsTemplateName(self,SmsTemplateName):
		self.add_query_param('SmsTemplateName',SmsTemplateName)

	def get_AndroidPopupBody(self):
		return self.get_query_params().get('AndroidPopupBody')

	def set_AndroidPopupBody(self,AndroidPopupBody):
		self.add_query_param('AndroidPopupBody',AndroidPopupBody)

	def get_iOSSilentNotification(self):
		return self.get_query_params().get('iOSSilentNotification')

	def set_iOSSilentNotification(self,iOSSilentNotification):
		self.add_query_param('iOSSilentNotification',iOSSilentNotification)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_AndroidNotificationChannel(self):
		return self.get_query_params().get('AndroidNotificationChannel')

	def set_AndroidNotificationChannel(self,AndroidNotificationChannel):
		self.add_query_param('AndroidNotificationChannel',AndroidNotificationChannel)

	def get_AndroidRemind(self):
		return self.get_query_params().get('AndroidRemind')

	def set_AndroidRemind(self,AndroidRemind):
		self.add_query_param('AndroidRemind',AndroidRemind)

	def get_AndroidActivity(self):
		return self.get_query_params().get('AndroidActivity')

	def set_AndroidActivity(self,AndroidActivity):
		self.add_query_param('AndroidActivity',AndroidActivity)

	def get_SmsSignName(self):
		return self.get_query_params().get('SmsSignName')

	def set_SmsSignName(self,SmsSignName):
		self.add_query_param('SmsSignName',SmsSignName)

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)

	def get_TargetValue(self):
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self,TargetValue):
		self.add_query_param('TargetValue',TargetValue)

	def get_AndroidXiaoMiActivity(self):
		return self.get_query_params().get('AndroidXiaoMiActivity')

	def set_AndroidXiaoMiActivity(self,AndroidXiaoMiActivity):
		self.add_query_param('AndroidXiaoMiActivity',AndroidXiaoMiActivity)

	def get_AndroidXiaoMiNotifyTitle(self):
		return self.get_query_params().get('AndroidXiaoMiNotifyTitle')

	def set_AndroidXiaoMiNotifyTitle(self,AndroidXiaoMiNotifyTitle):
		self.add_query_param('AndroidXiaoMiNotifyTitle',AndroidXiaoMiNotifyTitle)