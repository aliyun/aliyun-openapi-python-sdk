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
from aliyunsdkelasticsearch.endpoint import endpoint_data

class UpgradeEngineVersionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'UpgradeEngineVersion','elasticsearch')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/actions/upgrade-version')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_dryRun(self):
		return self.get_query_params().get('dryRun')

	def set_dryRun(self,dryRun):
		self.add_query_param('dryRun',dryRun)

	def get_clientToken(self):
		return self.get_query_params().get('clientToken')

	def set_clientToken(self,clientToken):
		self.add_query_param('clientToken',clientToken)

	def get_type(self):
		return self.get_body_params().get('type')

	def set_type(self,type):
		self.add_body_params('type', type)

	def get_version(self):
		return self.get_body_params().get('version')

	def set_version(self,version):
		self.add_body_params('version', version)