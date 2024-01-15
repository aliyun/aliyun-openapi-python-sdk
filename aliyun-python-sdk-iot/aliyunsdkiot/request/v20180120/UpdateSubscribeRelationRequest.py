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

class UpdateSubscribeRelationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'UpdateSubscribeRelation','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OtaEventFlag(self):
		return self.get_query_params().get('OtaEventFlag')

	def set_OtaEventFlag(self,OtaEventFlag):
		self.add_query_param('OtaEventFlag',OtaEventFlag)

	def get_DeviceTopoLifeCycleFlag(self):
		return self.get_query_params().get('DeviceTopoLifeCycleFlag')

	def set_DeviceTopoLifeCycleFlag(self,DeviceTopoLifeCycleFlag):
		self.add_query_param('DeviceTopoLifeCycleFlag',DeviceTopoLifeCycleFlag)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_DeviceLifeCycleFlag(self):
		return self.get_query_params().get('DeviceLifeCycleFlag')

	def set_DeviceLifeCycleFlag(self,DeviceLifeCycleFlag):
		self.add_query_param('DeviceLifeCycleFlag',DeviceLifeCycleFlag)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_DeviceStatusChangeFlag(self):
		return self.get_query_params().get('DeviceStatusChangeFlag')

	def set_DeviceStatusChangeFlag(self,DeviceStatusChangeFlag):
		self.add_query_param('DeviceStatusChangeFlag',DeviceStatusChangeFlag)

	def get_OtaVersionFlag(self):
		return self.get_query_params().get('OtaVersionFlag')

	def set_OtaVersionFlag(self,OtaVersionFlag):
		self.add_query_param('OtaVersionFlag',OtaVersionFlag)

	def get_DeviceTagFlag(self):
		return self.get_query_params().get('DeviceTagFlag')

	def set_DeviceTagFlag(self,DeviceTagFlag):
		self.add_query_param('DeviceTagFlag',DeviceTagFlag)

	def get_ConsumerGroupIdss(self):
		return self.get_query_params().get('ConsumerGroupIds')

	def set_ConsumerGroupIdss(self, ConsumerGroupIdss):
		for depth1 in range(len(ConsumerGroupIdss)):
			if ConsumerGroupIdss[depth1] is not None:
				self.add_query_param('ConsumerGroupIds.' + str(depth1 + 1) , ConsumerGroupIdss[depth1])

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_ThingHistoryFlag(self):
		return self.get_query_params().get('ThingHistoryFlag')

	def set_ThingHistoryFlag(self,ThingHistoryFlag):
		self.add_query_param('ThingHistoryFlag',ThingHistoryFlag)

	def get_FoundDeviceListFlag(self):
		return self.get_query_params().get('FoundDeviceListFlag')

	def set_FoundDeviceListFlag(self,FoundDeviceListFlag):
		self.add_query_param('FoundDeviceListFlag',FoundDeviceListFlag)

	def get_OtaJobFlag(self):
		return self.get_query_params().get('OtaJobFlag')

	def set_OtaJobFlag(self,OtaJobFlag):
		self.add_query_param('OtaJobFlag',OtaJobFlag)

	def get_SubscribeFlags(self):
		return self.get_query_params().get('SubscribeFlags')

	def set_SubscribeFlags(self,SubscribeFlags):
		self.add_query_param('SubscribeFlags',SubscribeFlags)

	def get_DeviceDataFlag(self):
		return self.get_query_params().get('DeviceDataFlag')

	def set_DeviceDataFlag(self,DeviceDataFlag):
		self.add_query_param('DeviceDataFlag',DeviceDataFlag)

	def get_MnsConfiguration(self):
		return self.get_query_params().get('MnsConfiguration')

	def set_MnsConfiguration(self,MnsConfiguration):
		self.add_query_param('MnsConfiguration',MnsConfiguration)