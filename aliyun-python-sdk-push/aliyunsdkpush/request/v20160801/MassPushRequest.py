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

class MassPushRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'MassPush')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PushTasks(self):
		return self.get_body_params().get('PushTasks')

	def set_PushTasks(self,PushTasks):
		for i in range(len(PushTasks)):	
			if PushTasks[i].get('AndroidNotificationBarType') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidNotificationBarType' , PushTasks[i].get('AndroidNotificationBarType'))
			if PushTasks[i].get('AndroidExtParameters') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidExtParameters' , PushTasks[i].get('AndroidExtParameters'))
			if PushTasks[i].get('iOSBadge') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSBadge' , PushTasks[i].get('iOSBadge'))
			if PushTasks[i].get('iOSBadgeAutoIncrement') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSBadgeAutoIncrement' , PushTasks[i].get('iOSBadgeAutoIncrement'))
			if PushTasks[i].get('AndroidOpenType') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidOpenType' , PushTasks[i].get('AndroidOpenType'))
			if PushTasks[i].get('Title') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.Title' , PushTasks[i].get('Title'))
			if PushTasks[i].get('Body') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.Body' , PushTasks[i].get('Body'))
			if PushTasks[i].get('DeviceType') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.DeviceType' , PushTasks[i].get('DeviceType'))
			if PushTasks[i].get('PushTime') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.PushTime' , PushTasks[i].get('PushTime'))
			if PushTasks[i].get('SendSpeed') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.SendSpeed' , PushTasks[i].get('SendSpeed'))
			if PushTasks[i].get('AndroidPopupActivity') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidPopupActivity' , PushTasks[i].get('AndroidPopupActivity'))
			if PushTasks[i].get('iOSRemindBody') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSRemindBody' , PushTasks[i].get('iOSRemindBody'))
			if PushTasks[i].get('iOSExtParameters') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSExtParameters' , PushTasks[i].get('iOSExtParameters'))
			if PushTasks[i].get('AndroidNotifyType') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidNotifyType' , PushTasks[i].get('AndroidNotifyType'))
			if PushTasks[i].get('AndroidPopupTitle') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidPopupTitle' , PushTasks[i].get('AndroidPopupTitle'))
			if PushTasks[i].get('iOSMusic') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSMusic' , PushTasks[i].get('iOSMusic'))
			if PushTasks[i].get('iOSApnsEnv') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSApnsEnv' , PushTasks[i].get('iOSApnsEnv'))
			if PushTasks[i].get('iOSMutableContent') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSMutableContent' , PushTasks[i].get('iOSMutableContent'))
			if PushTasks[i].get('AndroidNotificationBarPriority') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidNotificationBarPriority' , PushTasks[i].get('AndroidNotificationBarPriority'))
			if PushTasks[i].get('ExpireTime') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.ExpireTime' , PushTasks[i].get('ExpireTime'))
			if PushTasks[i].get('AndroidPopupBody') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidPopupBody' , PushTasks[i].get('AndroidPopupBody'))
			if PushTasks[i].get('iOSNotificationCategory') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSNotificationCategory' , PushTasks[i].get('iOSNotificationCategory'))
			if PushTasks[i].get('StoreOffline') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.StoreOffline' , PushTasks[i].get('StoreOffline'))
			if PushTasks[i].get('iOSSilentNotification') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSSilentNotification' , PushTasks[i].get('iOSSilentNotification'))
			if PushTasks[i].get('JobKey') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.JobKey' , PushTasks[i].get('JobKey'))
			if PushTasks[i].get('Target') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.Target' , PushTasks[i].get('Target'))
			if PushTasks[i].get('AndroidOpenUrl') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidOpenUrl' , PushTasks[i].get('AndroidOpenUrl'))
			if PushTasks[i].get('AndroidNotificationChannel') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidNotificationChannel' , PushTasks[i].get('AndroidNotificationChannel'))
			if PushTasks[i].get('AndroidRemind') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidRemind' , PushTasks[i].get('AndroidRemind'))
			if PushTasks[i].get('AndroidActivity') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidActivity' , PushTasks[i].get('AndroidActivity'))
			if PushTasks[i].get('AndroidXiaoMiNotifyBody') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidXiaoMiNotifyBody' , PushTasks[i].get('AndroidXiaoMiNotifyBody'))
			if PushTasks[i].get('iOSSubtitle') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSSubtitle' , PushTasks[i].get('iOSSubtitle'))
			if PushTasks[i].get('iOSRemind') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.iOSRemind' , PushTasks[i].get('iOSRemind'))
			if PushTasks[i].get('TargetValue') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.TargetValue' , PushTasks[i].get('TargetValue'))
			if PushTasks[i].get('AndroidMusic') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidMusic' , PushTasks[i].get('AndroidMusic'))
			if PushTasks[i].get('AndroidXiaoMiActivity') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidXiaoMiActivity' , PushTasks[i].get('AndroidXiaoMiActivity'))
			if PushTasks[i].get('AndroidXiaoMiNotifyTitle') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.AndroidXiaoMiNotifyTitle' , PushTasks[i].get('AndroidXiaoMiNotifyTitle'))
			if PushTasks[i].get('PushType') is not None:
				self.add_body_params('PushTask.' + str(i + 1) + '.PushType' , PushTasks[i].get('PushType'))


	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)