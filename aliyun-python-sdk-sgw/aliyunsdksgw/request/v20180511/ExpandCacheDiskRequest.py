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

class ExpandCacheDiskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'ExpandCacheDisk','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LocalFilePath(self):
		return self.get_query_params().get('LocalFilePath')

	def set_LocalFilePath(self,LocalFilePath):
		self.add_query_param('LocalFilePath',LocalFilePath)

	def get_NewSizeInGB(self):
		return self.get_query_params().get('NewSizeInGB')

	def set_NewSizeInGB(self,NewSizeInGB):
		self.add_query_param('NewSizeInGB',NewSizeInGB)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_GatewayId(self):
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self,GatewayId):
		self.add_query_param('GatewayId',GatewayId)