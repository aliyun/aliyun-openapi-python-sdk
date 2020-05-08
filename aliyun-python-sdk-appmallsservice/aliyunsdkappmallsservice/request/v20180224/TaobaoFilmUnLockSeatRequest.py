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

class TaobaoFilmUnLockSeatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AppMallsService', '2018-02-24', 'TaobaoFilmUnLockSeat')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LockSeatApplyKey(self):
		return self.get_query_params().get('LockSeatApplyKey')

	def set_LockSeatApplyKey(self,LockSeatApplyKey):
		self.add_query_param('LockSeatApplyKey',LockSeatApplyKey)

	def get_ExtUserId(self):
		return self.get_query_params().get('ExtUserId')

	def set_ExtUserId(self,ExtUserId):
		self.add_query_param('ExtUserId',ExtUserId)

	def get_ParamsJson(self):
		return self.get_query_params().get('ParamsJson')

	def set_ParamsJson(self,ParamsJson):
		self.add_query_param('ParamsJson',ParamsJson)