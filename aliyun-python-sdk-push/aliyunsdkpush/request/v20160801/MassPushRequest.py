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

	def get_IdempotentToken(self): # String
		return self.get_query_params().get('IdempotentToken')

	def set_IdempotentToken(self, IdempotentToken):  # String
		self.add_query_param('IdempotentToken', IdempotentToken)
	def get_PushTasks(self): # RepeatList
		return self.get_body_params().get('PushTask')

	def set_PushTasks(self, PushTask):  # RepeatList
		for depth1 in range(len(PushTask)):
			if PushTask[depth1].get('AndroidNotificationBarType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationBarType', PushTask[depth1].get('AndroidNotificationBarType'))
			if PushTask[depth1].get('AndroidMessageOppoNotifyLevel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMessageOppoNotifyLevel', PushTask[depth1].get('AndroidMessageOppoNotifyLevel'))
			if PushTask[depth1].get('Body') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Body', PushTask[depth1].get('Body'))
			if PushTask[depth1].get('DeviceType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.DeviceType', PushTask[depth1].get('DeviceType'))
			if PushTask[depth1].get('PushTime') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.PushTime', PushTask[depth1].get('PushTime'))
			if PushTask[depth1].get('SendSpeed') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.SendSpeed', PushTask[depth1].get('SendSpeed'))
			if PushTask[depth1].get('AndroidNotificationHuaweiChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationHuaweiChannel', PushTask[depth1].get('AndroidNotificationHuaweiChannel'))
			if PushTask[depth1].get('AndroidPopupActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupActivity', PushTask[depth1].get('AndroidPopupActivity'))
			if PushTask[depth1].get('HarmonyNotifyId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyNotifyId', PushTask[depth1].get('HarmonyNotifyId'))
			if PushTask[depth1].get('HarmonyRenderStyle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyRenderStyle', PushTask[depth1].get('HarmonyRenderStyle'))
			if PushTask[depth1].get('iOSRemindBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSRemindBody', PushTask[depth1].get('iOSRemindBody'))
			if PushTask[depth1].get('Trim') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Trim', PushTask[depth1].get('Trim'))
			if PushTask[depth1].get('AndroidMessageVivoCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMessageVivoCategory', PushTask[depth1].get('AndroidMessageVivoCategory'))
			if PushTask[depth1].get('AndroidNotifyType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotifyType', PushTask[depth1].get('AndroidNotifyType'))
			if PushTask[depth1].get('AndroidPopupTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupTitle', PushTask[depth1].get('AndroidPopupTitle'))
			if PushTask[depth1].get('AndroidMessageHuaweiCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMessageHuaweiCategory', PushTask[depth1].get('AndroidMessageHuaweiCategory'))
			if PushTask[depth1].get('iOSMusic') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSMusic', PushTask[depth1].get('iOSMusic'))
			if PushTask[depth1].get('iOSApnsEnv') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSApnsEnv', PushTask[depth1].get('iOSApnsEnv'))
			if PushTask[depth1].get('iOSMutableContent') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSMutableContent', PushTask[depth1].get('iOSMutableContent'))
			if PushTask[depth1].get('AndroidNotificationBarPriority') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationBarPriority', PushTask[depth1].get('AndroidNotificationBarPriority'))
			if PushTask[depth1].get('ExpireTime') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.ExpireTime', PushTask[depth1].get('ExpireTime'))
			if PushTask[depth1].get('AndroidImageUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidImageUrl', PushTask[depth1].get('AndroidImageUrl'))
			if PushTask[depth1].get('AndroidNotificationThreadId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationThreadId', PushTask[depth1].get('AndroidNotificationThreadId'))
			if PushTask[depth1].get('AndroidHonorTargetUserType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidHonorTargetUserType', PushTask[depth1].get('AndroidHonorTargetUserType'))
			if PushTask[depth1].get('HarmonyRemindBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyRemindBody', PushTask[depth1].get('HarmonyRemindBody'))
			if PushTask[depth1].get('AndroidNotificationVivoChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationVivoChannel', PushTask[depth1].get('AndroidNotificationVivoChannel'))
			if PushTask[depth1].get('AndroidVivoReceiptId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidVivoReceiptId', PushTask[depth1].get('AndroidVivoReceiptId'))
			if PushTask[depth1].get('iOSNotificationCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSNotificationCategory', PushTask[depth1].get('iOSNotificationCategory'))
			if PushTask[depth1].get('AndroidNotificationXiaomiChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationXiaomiChannel', PushTask[depth1].get('AndroidNotificationXiaomiChannel'))
			if PushTask[depth1].get('HarmonyAction') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyAction', PushTask[depth1].get('HarmonyAction'))
			if PushTask[depth1].get('StoreOffline') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.StoreOffline', PushTask[depth1].get('StoreOffline'))
			if PushTask[depth1].get('iOSRelevanceScore') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSRelevanceScore', PushTask[depth1].get('iOSRelevanceScore'))
			if PushTask[depth1].get('AndroidVivoPushMode') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidVivoPushMode', PushTask[depth1].get('AndroidVivoPushMode'))
			if PushTask[depth1].get('AndroidInboxBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidInboxBody', PushTask[depth1].get('AndroidInboxBody'))
			if PushTask[depth1].get('JobKey') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.JobKey', PushTask[depth1].get('JobKey'))
			if PushTask[depth1].get('HarmonyReceiptId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyReceiptId', PushTask[depth1].get('HarmonyReceiptId'))
			if PushTask[depth1].get('AndroidOpenUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidOpenUrl', PushTask[depth1].get('AndroidOpenUrl'))
			if PushTask[depth1].get('AndroidBadgeSetNum') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBadgeSetNum', PushTask[depth1].get('AndroidBadgeSetNum'))
			if PushTask[depth1].get('AndroidXiaoMiNotifyBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiNotifyBody', PushTask[depth1].get('AndroidXiaoMiNotifyBody'))
			if PushTask[depth1].get('iOSSubtitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSSubtitle', PushTask[depth1].get('iOSSubtitle'))
			if PushTask[depth1].get('AndroidXiaomiBigPictureUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaomiBigPictureUrl', PushTask[depth1].get('AndroidXiaomiBigPictureUrl'))
			if PushTask[depth1].get('HarmonyCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyCategory', PushTask[depth1].get('HarmonyCategory'))
			if PushTask[depth1].get('iOSRemind') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSRemind', PushTask[depth1].get('iOSRemind'))
			if PushTask[depth1].get('iOSNotificationThreadId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSNotificationThreadId', PushTask[depth1].get('iOSNotificationThreadId'))
			if PushTask[depth1].get('AndroidHuaweiTargetUserType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidHuaweiTargetUserType', PushTask[depth1].get('AndroidHuaweiTargetUserType'))
			if PushTask[depth1].get('HarmonyRemind') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyRemind', PushTask[depth1].get('HarmonyRemind'))
			if PushTask[depth1].get('AndroidMusic') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMusic', PushTask[depth1].get('AndroidMusic'))
			if PushTask[depth1].get('HarmonyExtensionPush') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyExtensionPush', PushTask[depth1].get('HarmonyExtensionPush'))
			if PushTask[depth1].get('iOSNotificationCollapseId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSNotificationCollapseId', PushTask[depth1].get('iOSNotificationCollapseId'))
			if PushTask[depth1].get('AndroidMessageHuaweiUrgency') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMessageHuaweiUrgency', PushTask[depth1].get('AndroidMessageHuaweiUrgency'))
			if PushTask[depth1].get('PushType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.PushType', PushTask[depth1].get('PushType'))
			if PushTask[depth1].get('iOSInterruptionLevel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSInterruptionLevel', PushTask[depth1].get('iOSInterruptionLevel'))
			if PushTask[depth1].get('HarmonyExtensionExtraData') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyExtensionExtraData', PushTask[depth1].get('HarmonyExtensionExtraData'))
			if PushTask[depth1].get('AndroidExtParameters') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidExtParameters', PushTask[depth1].get('AndroidExtParameters'))
			if PushTask[depth1].get('HarmonyImageUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyImageUrl', PushTask[depth1].get('HarmonyImageUrl'))
			if PushTask[depth1].get('iOSBadge') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSBadge', PushTask[depth1].get('iOSBadge'))
			if PushTask[depth1].get('AndroidBigBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBigBody', PushTask[depth1].get('AndroidBigBody'))
			if PushTask[depth1].get('iOSBadgeAutoIncrement') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSBadgeAutoIncrement', PushTask[depth1].get('iOSBadgeAutoIncrement'))
			if PushTask[depth1].get('AndroidOpenType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidOpenType', PushTask[depth1].get('AndroidOpenType'))
			if PushTask[depth1].get('HarmonyRemindTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyRemindTitle', PushTask[depth1].get('HarmonyRemindTitle'))
			if PushTask[depth1].get('Title') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Title', PushTask[depth1].get('Title'))
			if PushTask[depth1].get('AndroidBadgeClass') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBadgeClass', PushTask[depth1].get('AndroidBadgeClass'))
			if PushTask[depth1].get('HarmonyBadgeAddNum') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyBadgeAddNum', PushTask[depth1].get('HarmonyBadgeAddNum'))
			if PushTask[depth1].get('HarmonyTestMessage') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyTestMessage', PushTask[depth1].get('HarmonyTestMessage'))
			if PushTask[depth1].get('AndroidRenderStyle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidRenderStyle', PushTask[depth1].get('AndroidRenderStyle'))
			if PushTask[depth1].get('iOSExtParameters') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSExtParameters', PushTask[depth1].get('iOSExtParameters'))
			if PushTask[depth1].get('AndroidBadgeAddNum') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBadgeAddNum', PushTask[depth1].get('AndroidBadgeAddNum'))
			if PushTask[depth1].get('AndroidHuaweiReceiptId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidHuaweiReceiptId', PushTask[depth1].get('AndroidHuaweiReceiptId'))
			if PushTask[depth1].get('AndroidNotificationHonorChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationHonorChannel', PushTask[depth1].get('AndroidNotificationHonorChannel'))
			if PushTask[depth1].get('AndroidXiaomiImageUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaomiImageUrl', PushTask[depth1].get('AndroidXiaomiImageUrl'))
			if PushTask[depth1].get('AndroidTargetUserType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidTargetUserType', PushTask[depth1].get('AndroidTargetUserType'))
			if PushTask[depth1].get('HarmonyUri') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyUri', PushTask[depth1].get('HarmonyUri'))
			if PushTask[depth1].get('AndroidPopupBody') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidPopupBody', PushTask[depth1].get('AndroidPopupBody'))
			if PushTask[depth1].get('HarmonyExtParameters') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyExtParameters', PushTask[depth1].get('HarmonyExtParameters'))
			if PushTask[depth1].get('AndroidBigPictureUrl') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBigPictureUrl', PushTask[depth1].get('AndroidBigPictureUrl'))
			if PushTask[depth1].get('iOSSilentNotification') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.iOSSilentNotification', PushTask[depth1].get('iOSSilentNotification'))
			if PushTask[depth1].get('AndroidNotificationGroup') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationGroup', PushTask[depth1].get('AndroidNotificationGroup'))
			if PushTask[depth1].get('SendChannels') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.SendChannels', PushTask[depth1].get('SendChannels'))
			if PushTask[depth1].get('HarmonyActionType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyActionType', PushTask[depth1].get('HarmonyActionType'))
			if PushTask[depth1].get('Target') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.Target', PushTask[depth1].get('Target'))
			if PushTask[depth1].get('HarmonyNotificationSlotType') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyNotificationSlotType', PushTask[depth1].get('HarmonyNotificationSlotType'))
			if PushTask[depth1].get('AndroidBigTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidBigTitle', PushTask[depth1].get('AndroidBigTitle'))
			if PushTask[depth1].get('AndroidNotificationChannel') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationChannel', PushTask[depth1].get('AndroidNotificationChannel'))
			if PushTask[depth1].get('AndroidRemind') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidRemind', PushTask[depth1].get('AndroidRemind'))
			if PushTask[depth1].get('HarmonyInboxContent') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyInboxContent', PushTask[depth1].get('HarmonyInboxContent'))
			if PushTask[depth1].get('AndroidActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidActivity', PushTask[depth1].get('AndroidActivity'))
			if PushTask[depth1].get('AndroidMessageOppoCategory') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidMessageOppoCategory', PushTask[depth1].get('AndroidMessageOppoCategory'))
			if PushTask[depth1].get('AndroidNotificationNotifyId') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidNotificationNotifyId', PushTask[depth1].get('AndroidNotificationNotifyId'))
			if PushTask[depth1].get('TargetValue') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.TargetValue', PushTask[depth1].get('TargetValue'))
			if PushTask[depth1].get('HarmonyBadgeSetNum') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.HarmonyBadgeSetNum', PushTask[depth1].get('HarmonyBadgeSetNum'))
			if PushTask[depth1].get('AndroidXiaoMiNotifyTitle') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiNotifyTitle', PushTask[depth1].get('AndroidXiaoMiNotifyTitle'))
			if PushTask[depth1].get('AndroidXiaoMiActivity') is not None:
				self.add_body_params('PushTask.' + str(depth1 + 1) + '.AndroidXiaoMiActivity', PushTask[depth1].get('AndroidXiaoMiActivity'))
	def get_AppKey(self): # Long
		return self.get_query_params().get('AppKey')

	def set_AppKey(self, AppKey):  # Long
		self.add_query_param('AppKey', AppKey)
