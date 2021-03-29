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

class InsertSwimmingLaneRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertSwimmingLane','Edas')
		self.set_uri_pattern('/pop/v5/trafficmgnt/swimming_lanes')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppInfos(self):
		return self.get_query_params().get('AppInfos')

	def set_AppInfos(self,AppInfos):
		self.add_query_param('AppInfos',AppInfos)

	def get_EntryRules(self):
		return self.get_query_params().get('EntryRules')

	def set_EntryRules(self,EntryRules):
		self.add_query_param('EntryRules',EntryRules)

	def get_LogicalRegionId(self):
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self,LogicalRegionId):
		self.add_query_param('LogicalRegionId',LogicalRegionId)

	def get_EnableRules(self):
		return self.get_query_params().get('EnableRules')

	def set_EnableRules(self,EnableRules):
		self.add_query_param('EnableRules',EnableRules)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Tag(self):
		return self.get_query_params().get('Tag')

	def set_Tag(self,Tag):
		self.add_query_param('Tag',Tag)