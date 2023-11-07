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
from aliyunsdkdrds.endpoint import endpoint_data

class UpdatePrivateRdsClassRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'UpdatePrivateRdsClass','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Storage(self): # String
		return self.get_query_params().get('Storage')

	def set_Storage(self, Storage):  # String
		self.add_query_param('Storage', Storage)
	def get_AutoUseCoupon(self): # Boolean
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # Boolean
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
	def get_RdsClass(self): # String
		return self.get_query_params().get('RdsClass')

	def set_RdsClass(self, RdsClass):  # String
		self.add_query_param('RdsClass', RdsClass)
	def get_PrePayDuration(self): # Integer
		return self.get_query_params().get('PrePayDuration')

	def set_PrePayDuration(self, PrePayDuration):  # Integer
		self.add_query_param('PrePayDuration', PrePayDuration)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
