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
from aliyunsdklinkedmall.endpoint import endpoint_data

class ReserveMovieSeatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'ReserveMovieSeat','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SeatIds(self):
		return self.get_query_params().get('SeatIds')

	def set_SeatIds(self,SeatIds):
		self.add_query_param('SeatIds',SeatIds)

	def get_BizUid(self):
		return self.get_query_params().get('BizUid')

	def set_BizUid(self,BizUid):
		self.add_query_param('BizUid',BizUid)

	def get_ExtJson(self):
		return self.get_query_params().get('ExtJson')

	def set_ExtJson(self,ExtJson):
		self.add_query_param('ExtJson',ExtJson)

	def get_Mobile(self):
		return self.get_query_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_query_param('Mobile',Mobile)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_SeatNames(self):
		return self.get_query_params().get('SeatNames')

	def set_SeatNames(self,SeatNames):
		self.add_query_param('SeatNames',SeatNames)

	def get_ScheduleId(self):
		return self.get_query_params().get('ScheduleId')

	def set_ScheduleId(self,ScheduleId):
		self.add_query_param('ScheduleId',ScheduleId)