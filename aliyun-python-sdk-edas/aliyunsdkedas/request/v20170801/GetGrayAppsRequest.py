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
from aliyunsdkedas.endpoint import endpoint_data

class GetGrayAppsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'GetGrayApps','Edas')
		self.set_uri_pattern('/pop/v5/gray/app_list')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterTypes(self):
		return self.get_query_params().get('ClusterTypes')

	def set_ClusterTypes(self,ClusterTypes):
		self.add_query_param('ClusterTypes',ClusterTypes)

	def get_Appname(self):
		return self.get_query_params().get('Appname')

	def set_Appname(self,Appname):
		self.add_query_param('Appname',Appname)

	def get_PhysicalRegionId(self):
		return self.get_query_params().get('PhysicalRegionId')

	def set_PhysicalRegionId(self,PhysicalRegionId):
		self.add_query_param('PhysicalRegionId',PhysicalRegionId)