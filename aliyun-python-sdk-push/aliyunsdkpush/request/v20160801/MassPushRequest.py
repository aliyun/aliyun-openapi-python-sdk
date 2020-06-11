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
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PushTasks(self):
		return self.get_body_params().get('PushTasks')

	def set_PushTasks(self, PushTasks):
		for depth1 in range(len(PushTasks)):
			if PushTasks[depth1].get('AndroidNotificationBarType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationBarType', PushTasks[depth1].get('AndroidNotificationBarType'))
			if PushTasks[depth1].get('AndroidExtParameters') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidExtParameters', PushTasks[depth1].get('AndroidExtParameters'))
			if PushTasks[depth1].get('iOSBadge') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSBadge', PushTasks[depth1].get('iOSBadge'))
			if PushTasks[depth1].get('iOSBadgeAutoIncrement') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSBadgeAutoIncrement', PushTasks[depth1].get('iOSBadgeAutoIncrement'))
			if PushTasks[depth1].get('AndroidOpenType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidOpenType', PushTasks[depth1].get('AndroidOpenType'))
			if PushTasks[depth1].get('Title') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Title', PushTasks[depth1].get('Title'))
			if PushTasks[depth1].get('Body') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Body', PushTasks[depth1].get('Body'))
			if PushTasks[depth1].get('DeviceType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.DeviceType', PushTasks[depth1].get('DeviceType'))
			if PushTasks[depth1].get('PushTime') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.PushTime', PushTasks[depth1].get('PushTime'))
			if PushTasks[depth1].get('SendSpeed') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.SendSpeed', PushTasks[depth1].get('SendSpeed'))
			if PushTasks[depth1].get('AndroidPopupActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupActivity', PushTasks[depth1].get('AndroidPopupActivity'))
			if PushTasks[depth1].get('iOSRemindBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSRemindBody', PushTasks[depth1].get('iOSRemindBody'))
			if PushTasks[depth1].get('iOSExtParameters') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSExtParameters', PushTasks[depth1].get('iOSExtParameters'))
			if PushTasks[depth1].get('AndroidNotifyType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotifyType', PushTasks[depth1].get('AndroidNotifyType'))
			if PushTasks[depth1].get('AndroidPopupTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupTitle', PushTasks[depth1].get('AndroidPopupTitle'))
			if PushTasks[depth1].get('iOSMusic') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSMusic', PushTasks[depth1].get('iOSMusic'))
			if PushTasks[depth1].get('iOSApnsEnv') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSApnsEnv', PushTasks[depth1].get('iOSApnsEnv'))
			if PushTasks[depth1].get('iOSMutableContent') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSMutableContent', PushTasks[depth1].get('iOSMutableContent'))
			if PushTasks[depth1].get('AndroidNotificationBarPriority') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationBarPriority', PushTasks[depth1].get('AndroidNotificationBarPriority'))
			if PushTasks[depth1].get('ExpireTime') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.ExpireTime', PushTasks[depth1].get('ExpireTime'))
			if PushTasks[depth1].get('AndroidNotificationVivoChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationVivoChannel', PushTasks[depth1].get('AndroidNotificationVivoChannel'))
			if PushTasks[depth1].get('AndroidPopupBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupBody', PushTasks[depth1].get('AndroidPopupBody'))
			if PushTasks[depth1].get('iOSNotificationCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSNotificationCategory', PushTasks[depth1].get('iOSNotificationCategory'))
			if PushTasks[depth1].get('AndroidNotificationXiaomiChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationXiaomiChannel', PushTasks[depth1].get('AndroidNotificationXiaomiChannel'))
			if PushTasks[depth1].get('StoreOffline') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.StoreOffline', PushTasks[depth1].get('StoreOffline'))
			if PushTasks[depth1].get('iOSSilentNotification') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSSilentNotification', PushTasks[depth1].get('iOSSilentNotification'))
			if PushTasks[depth1].get('JobKey') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.JobKey', PushTasks[depth1].get('JobKey'))
			if PushTasks[depth1].get('Target') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Target', PushTasks[depth1].get('Target'))
			if PushTasks[depth1].get('AndroidOpenUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidOpenUrl', PushTasks[depth1].get('AndroidOpenUrl'))
			if PushTasks[depth1].get('AndroidNotificationChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationChannel', PushTasks[depth1].get('AndroidNotificationChannel'))
			if PushTasks[depth1].get('AndroidRemind') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidRemind', PushTasks[depth1].get('AndroidRemind'))
			if PushTasks[depth1].get('AndroidActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidActivity', PushTasks[depth1].get('AndroidActivity'))
			if PushTasks[depth1].get('AndroidXiaoMiNotifyBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiNotifyBody', PushTasks[depth1].get('AndroidXiaoMiNotifyBody'))
			if PushTasks[depth1].get('iOSSubtitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSSubtitle', PushTasks[depth1].get('iOSSubtitle'))
			if PushTasks[depth1].get('iOSRemind') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSRemind', PushTasks[depth1].get('iOSRemind'))
			if PushTasks[depth1].get('TargetValue') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.TargetValue', PushTasks[depth1].get('TargetValue'))
			if PushTasks[depth1].get('AndroidMusic') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMusic', PushTasks[depth1].get('AndroidMusic'))
			if PushTasks[depth1].get('AndroidXiaoMiActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiActivity', PushTasks[depth1].get('AndroidXiaoMiActivity'))
			if PushTasks[depth1].get('AndroidXiaoMiNotifyTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiNotifyTitle', PushTasks[depth1].get('AndroidXiaoMiNotifyTitle'))
			if PushTasks[depth1].get('PushType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.PushType', PushTasks[depth1].get('PushType'))

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)