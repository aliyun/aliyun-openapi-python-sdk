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
from aliyunsdkiot.endpoint import endpoint_data

class AddDeviceToSharePromotionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'AddDeviceToSharePromotion','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SharePromotionActivityId(self):
		return self.get_body_params().get('SharePromotionActivityId')

	def set_SharePromotionActivityId(self,SharePromotionActivityId):
		self.add_body_params('SharePromotionActivityId', SharePromotionActivityId)

	def get_DeviceSimpleInfoLists(self):
		return self.get_body_params().get('DeviceSimpleInfoList')

	def set_DeviceSimpleInfoLists(self, DeviceSimpleInfoLists):
		for depth1 in range(len(DeviceSimpleInfoLists)):
			if DeviceSimpleInfoLists[depth1].get('DeviceName') is not None:
				self.add_body_params('DeviceSimpleInfoList.' + str(depth1 + 1) + '.DeviceName', DeviceSimpleInfoLists[depth1].get('DeviceName'))
			if DeviceSimpleInfoLists[depth1].get('ProductKey') is not None:
				self.add_body_params('DeviceSimpleInfoList.' + str(depth1 + 1) + '.ProductKey', DeviceSimpleInfoLists[depth1].get('ProductKey'))

	def get_IotInstanceId(self):
		return self.get_body_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_body_params('IotInstanceId', IotInstanceId)

	def get_ShareTaskCode(self):
		return self.get_body_params().get('ShareTaskCode')

	def set_ShareTaskCode(self,ShareTaskCode):
		self.add_body_params('ShareTaskCode', ShareTaskCode)