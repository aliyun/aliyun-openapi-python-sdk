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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkeas.endpoint import endpoint_data

class DeleteGatewayIntranetLinkedVpcRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2021-07-01', 'DeleteGatewayIntranetLinkedVpc','eas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/gateways/[ClusterId]/[GatewayId]/intranet_endpoint_linked_vpc')
		self.set_method('DELETE')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ClusterId(self): # String
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_path_param('ClusterId', ClusterId)
	def get_GatewayId(self): # String
		return self.get_path_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_path_param('GatewayId', GatewayId)
