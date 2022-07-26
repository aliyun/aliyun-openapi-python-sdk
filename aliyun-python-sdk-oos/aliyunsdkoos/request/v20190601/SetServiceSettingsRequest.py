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
from aliyunsdkoos.endpoint import endpoint_data

class SetServiceSettingsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'SetServiceSettings','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DeliverySlsEnabled(self): # Boolean
		return self.get_query_params().get('DeliverySlsEnabled')

	def set_DeliverySlsEnabled(self, DeliverySlsEnabled):  # Boolean
		self.add_query_param('DeliverySlsEnabled', DeliverySlsEnabled)
	def get_RdcEnterpriseId(self): # String
		return self.get_query_params().get('RdcEnterpriseId')

	def set_RdcEnterpriseId(self, RdcEnterpriseId):  # String
		self.add_query_param('RdcEnterpriseId', RdcEnterpriseId)
	def get_DeliveryOssKeyPrefix(self): # String
		return self.get_query_params().get('DeliveryOssKeyPrefix')

	def set_DeliveryOssKeyPrefix(self, DeliveryOssKeyPrefix):  # String
		self.add_query_param('DeliveryOssKeyPrefix', DeliveryOssKeyPrefix)
	def get_DeliveryOssEnabled(self): # Boolean
		return self.get_query_params().get('DeliveryOssEnabled')

	def set_DeliveryOssEnabled(self, DeliveryOssEnabled):  # Boolean
		self.add_query_param('DeliveryOssEnabled', DeliveryOssEnabled)
	def get_DeliverySlsProjectName(self): # String
		return self.get_query_params().get('DeliverySlsProjectName')

	def set_DeliverySlsProjectName(self, DeliverySlsProjectName):  # String
		self.add_query_param('DeliverySlsProjectName', DeliverySlsProjectName)
	def get_DeliveryOssBucketName(self): # String
		return self.get_query_params().get('DeliveryOssBucketName')

	def set_DeliveryOssBucketName(self, DeliveryOssBucketName):  # String
		self.add_query_param('DeliveryOssBucketName', DeliveryOssBucketName)
