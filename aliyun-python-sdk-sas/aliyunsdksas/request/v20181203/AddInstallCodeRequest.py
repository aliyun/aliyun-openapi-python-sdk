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
from aliyunsdksas.endpoint import endpoint_data

class AddInstallCodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'AddInstallCode','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExpiredDate(self): # Long
		return self.get_query_params().get('ExpiredDate')

	def set_ExpiredDate(self, ExpiredDate):  # Long
		self.add_query_param('ExpiredDate', ExpiredDate)
	def get_Os(self): # String
		return self.get_query_params().get('Os')

	def set_Os(self, Os):  # String
		self.add_query_param('Os', Os)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_ProxyCluster(self): # String
		return self.get_query_params().get('ProxyCluster')

	def set_ProxyCluster(self, ProxyCluster):  # String
		self.add_query_param('ProxyCluster', ProxyCluster)
	def get_OnlyImage(self): # Boolean
		return self.get_query_params().get('OnlyImage')

	def set_OnlyImage(self, OnlyImage):  # Boolean
		self.add_query_param('OnlyImage', OnlyImage)
	def get_VendorName(self): # String
		return self.get_query_params().get('VendorName')

	def set_VendorName(self, VendorName):  # String
		self.add_query_param('VendorName', VendorName)
