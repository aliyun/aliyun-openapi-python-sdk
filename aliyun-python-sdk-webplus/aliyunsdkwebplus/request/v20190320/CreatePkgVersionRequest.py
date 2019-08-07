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
from aliyunsdkwebplus.endpoint import endpoint_data

class CreatePkgVersionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'CreatePkgVersion','webx')
		self.set_uri_pattern('/pop/v1/wam/pkgVersion')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PackageSource(self):
		return self.get_body_params().get('PackageSource')

	def set_PackageSource(self,PackageSource):
		self.add_body_params('PackageSource', PackageSource)

	def get_PkgVersionLabel(self):
		return self.get_body_params().get('PkgVersionLabel')

	def set_PkgVersionLabel(self,PkgVersionLabel):
		self.add_body_params('PkgVersionLabel', PkgVersionLabel)

	def get_PkgVersionDescription(self):
		return self.get_body_params().get('PkgVersionDescription')

	def set_PkgVersionDescription(self,PkgVersionDescription):
		self.add_body_params('PkgVersionDescription', PkgVersionDescription)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)