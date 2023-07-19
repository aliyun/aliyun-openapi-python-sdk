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
from aliyunsdkdts.endpoint import endpoint_data

class InitDtsRdsInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'InitDtsRdsInstance','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndpointInstanceId(self): # String
		return self.get_query_params().get('EndpointInstanceId')

	def set_EndpointInstanceId(self, EndpointInstanceId):  # String
		self.add_query_param('EndpointInstanceId', EndpointInstanceId)
	def get_EndpointRegion(self): # String
		return self.get_query_params().get('EndpointRegion')

	def set_EndpointRegion(self, EndpointRegion):  # String
		self.add_query_param('EndpointRegion', EndpointRegion)
	def get_EndpointCenId(self): # String
		return self.get_query_params().get('EndpointCenId')

	def set_EndpointCenId(self, EndpointCenId):  # String
		self.add_query_param('EndpointCenId', EndpointCenId)
	def get_EndpointInstanceType(self): # String
		return self.get_query_params().get('EndpointInstanceType')

	def set_EndpointInstanceType(self, EndpointInstanceType):  # String
		self.add_query_param('EndpointInstanceType', EndpointInstanceType)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
