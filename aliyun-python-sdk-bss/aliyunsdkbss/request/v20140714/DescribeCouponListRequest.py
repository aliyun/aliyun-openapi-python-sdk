# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeCouponListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Bss', '2014-07-14', 'DescribeCouponList')
		self.set_protocol_type(self, 'https');

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_StartDeliveryTime(self):
		return self.get_query_params().get('StartDeliveryTime')

	def set_StartDeliveryTime(self,StartDeliveryTime):
		self.add_query_param('StartDeliveryTime',StartDeliveryTime)

	def get_EndDeliveryTime(self):
		return self.get_query_params().get('EndDeliveryTime')

	def set_EndDeliveryTime(self,EndDeliveryTime):
		self.add_query_param('EndDeliveryTime',EndDeliveryTime)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)