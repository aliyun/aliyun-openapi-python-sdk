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
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'SaveWebRTCStats')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CallId(self):
		return self.get_query_params().get('CallId')

	def set_CallId(self,CallId):
		self.add_query_param('CallId',CallId)

	def get_RecordTime(self):
		return self.get_query_params().get('RecordTime')

	def set_RecordTime(self,RecordTime):
		self.add_query_param('RecordTime',RecordTime)

	def get_CallStartTime(self):
		return self.get_query_params().get('CallStartTime')

	def set_CallStartTime(self,CallStartTime):
		self.add_query_param('CallStartTime',CallStartTime)

	def get_Uid(self):
		return self.get_query_params().get('Uid')

	def set_Uid(self,Uid):
		self.add_query_param('Uid',Uid)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Stats(self):
		return self.get_query_params().get('Stats')

	def set_Stats(self,Stats):
		self.add_query_param('Stats',Stats)

	def get_TenantId(self):
		return self.get_query_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_query_param('TenantId',TenantId)

	def get_CalleeNumber(self):
		return self.get_query_params().get('CalleeNumber')

	def set_CalleeNumber(self,CalleeNumber):
		self.add_query_param('CalleeNumber',CalleeNumber)

	def get_CallerNumber(self):
		return self.get_query_params().get('CallerNumber')

	def set_CallerNumber(self,CallerNumber):
		self.add_query_param('CallerNumber',CallerNumber)