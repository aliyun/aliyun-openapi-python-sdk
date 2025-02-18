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
from aliyunsdksgw.endpoint import endpoint_data

class ReportGatewayInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'ReportGatewayInfo','hcs_sgw')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientUUID(self): # String
		return self.get_query_params().get('ClientUUID')

	def set_ClientUUID(self, ClientUUID):  # String
		self.add_query_param('ClientUUID', ClientUUID)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_GatewayStatus(self): # String
		return self.get_query_params().get('GatewayStatus')

	def set_GatewayStatus(self, GatewayStatus):  # String
		self.add_query_param('GatewayStatus', GatewayStatus)
	def get_Time(self): # Long
		return self.get_query_params().get('Time')

	def set_Time(self, Time):  # Long
		self.add_query_param('Time', Time)
	def get_GatewayId(self): # String
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_query_param('GatewayId', GatewayId)
	def get_Info(self): # String
		return self.get_query_params().get('Info')

	def set_Info(self, Info):  # String
		self.add_query_param('Info', Info)
