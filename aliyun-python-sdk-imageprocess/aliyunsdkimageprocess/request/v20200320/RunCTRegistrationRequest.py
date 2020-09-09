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
from aliyunsdkimageprocess.endpoint import endpoint_data

class RunCTRegistrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageprocess', '2020-03-20', 'RunCTRegistration','imageprocess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DataSourceType(self):
		return self.get_body_params().get('DataSourceType')

	def set_DataSourceType(self,DataSourceType):
		self.add_body_params('DataSourceType', DataSourceType)

	def get_OrgName(self):
		return self.get_body_params().get('OrgName')

	def set_OrgName(self,OrgName):
		self.add_body_params('OrgName', OrgName)

	def get_ReferenceLists(self):
		return self.get_body_params().get('ReferenceList')

	def set_ReferenceLists(self, ReferenceLists):
		for depth1 in range(len(ReferenceLists)):
			if ReferenceLists[depth1].get('ReferenceURL') is not None:
				self.add_body_params('ReferenceList.' + str(depth1 + 1) + '.ReferenceURL', ReferenceLists[depth1].get('ReferenceURL'))

	def get_DataFormat(self):
		return self.get_body_params().get('DataFormat')

	def set_DataFormat(self,DataFormat):
		self.add_body_params('DataFormat', DataFormat)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_FloatingLists(self):
		return self.get_body_params().get('FloatingList')

	def set_FloatingLists(self, FloatingLists):
		for depth1 in range(len(FloatingLists)):
			if FloatingLists[depth1].get('FloatingURL') is not None:
				self.add_body_params('FloatingList.' + str(depth1 + 1) + '.FloatingURL', FloatingLists[depth1].get('FloatingURL'))