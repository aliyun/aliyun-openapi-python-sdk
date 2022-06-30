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

class ListRegionsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'apds', '2022-03-31', 'ListRegions')
		self.set_uri_pattern('/okss-services/winback/query-region')
		self.set_method('POST')

	def get_cloudType(self): # string
		return self.get_query_params().get('cloudType')

	def set_cloudType(self, cloudType):  # string
		self.add_query_param('cloudType', cloudType)
	def get_ak(self): # string
		return self.get_query_params().get('ak')

	def set_ak(self, ak):  # string
		self.add_query_param('ak', ak)
	def get_sk(self): # string
		return self.get_query_params().get('sk')

	def set_sk(self, sk):  # string
		self.add_query_param('sk', sk)
	def get_tenantId(self): # string
		return self.get_query_params().get('tenantId')

	def set_tenantId(self, tenantId):  # string
		self.add_query_param('tenantId', tenantId)
	def get_region(self): # string
		return self.get_query_params().get('region')

	def set_region(self, region):  # string
		self.add_query_param('region', region)
