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
from aliyunsdkmaxcompute.endpoint import endpoint_data

class UpdateQuotaPlanRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'MaxCompute', '2022-01-04', 'UpdateQuotaPlan')
		self.set_uri_pattern('/api/v1/quotas/[nickname]/plans/[planName]')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_nickname(self): # String
		return self.get_path_params().get('nickname')

	def set_nickname(self, nickname):  # String
		self.add_path_param('nickname', nickname)
	def get_planName(self): # String
		return self.get_path_params().get('planName')

	def set_planName(self, planName):  # String
		self.add_path_param('planName', planName)
	def get_tenantId(self): # String
		return self.get_query_params().get('tenantId')

	def set_tenantId(self, tenantId):  # String
		self.add_query_param('tenantId', tenantId)
	def get_region(self): # String
		return self.get_query_params().get('region')

	def set_region(self, region):  # String
		self.add_query_param('region', region)
	def get_body(self): # String
		return self.get_body_params().get('body')

	def set_body(self, body):  # String
		self.add_body_params('body', body)
