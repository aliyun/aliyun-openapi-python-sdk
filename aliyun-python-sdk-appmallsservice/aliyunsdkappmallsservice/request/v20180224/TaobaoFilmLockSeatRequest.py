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
from aliyunsdkappmallsservice.endpoint import endpoint_data

class TaobaoFilmLockSeatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AppMallsService', '2018-02-24', 'TaobaoFilmLockSeat')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ScheduleId(self):
		return self.get_query_params().get('ScheduleId')

	def set_ScheduleId(self,ScheduleId):
		self.add_query_param('ScheduleId',ScheduleId)

	def get_SeatIds(self):
		return self.get_query_params().get('SeatIds')

	def set_SeatIds(self,SeatIds):
		self.add_query_param('SeatIds',SeatIds)

	def get_SeatNames(self):
		return self.get_query_params().get('SeatNames')

	def set_SeatNames(self,SeatNames):
		self.add_query_param('SeatNames',SeatNames)

	def get_Mobile(self):
		return self.get_query_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_query_param('Mobile',Mobile)

	def get_ExtUserId(self):
		return self.get_query_params().get('ExtUserId')

	def set_ExtUserId(self,ExtUserId):
		self.add_query_param('ExtUserId',ExtUserId)

	def get_ParamsJson(self):
		return self.get_query_params().get('ParamsJson')

	def set_ParamsJson(self,ParamsJson):
		self.add_query_param('ParamsJson',ParamsJson)