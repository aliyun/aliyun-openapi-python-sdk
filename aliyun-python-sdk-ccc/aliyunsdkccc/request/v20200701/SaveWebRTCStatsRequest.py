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
from aliyunsdkccc.endpoint import endpoint_data

class SaveWebRTCStatsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'SaveWebRTCStats')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CallId(self):
		return self.get_query_params().get('CallId')

	def set_CallId(self,CallId):
		self.add_query_param('CallId',CallId)

	def get_SenderReport(self):
		return self.get_query_params().get('SenderReport')

	def set_SenderReport(self,SenderReport):
		self.add_query_param('SenderReport',SenderReport)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ReceiverReport(self):
		return self.get_query_params().get('ReceiverReport')

	def set_ReceiverReport(self,ReceiverReport):
		self.add_query_param('ReceiverReport',ReceiverReport)

	def get_GoogAddress(self):
		return self.get_query_params().get('GoogAddress')

	def set_GoogAddress(self,GoogAddress):
		self.add_query_param('GoogAddress',GoogAddress)

	def get_GeneralInfo(self):
		return self.get_query_params().get('GeneralInfo')

	def set_GeneralInfo(self,GeneralInfo):
		self.add_query_param('GeneralInfo',GeneralInfo)