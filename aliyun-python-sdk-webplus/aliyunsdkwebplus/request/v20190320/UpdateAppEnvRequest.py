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

class UpdateAppEnvRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'UpdateAppEnv','webx')
		self.set_uri_pattern('/pop/v1/wam/appEnv')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OptionSettings(self):
		return self.get_body_params().get('OptionSettings')

	def set_OptionSettings(self,OptionSettings):
		self.add_body_params('OptionSettings', OptionSettings)

	def get_DryRun(self):
		return self.get_body_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_body_params('DryRun', DryRun)

	def get_StackId(self):
		return self.get_body_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_body_params('StackId', StackId)

	def get_EnvDescription(self):
		return self.get_body_params().get('EnvDescription')

	def set_EnvDescription(self,EnvDescription):
		self.add_body_params('EnvDescription', EnvDescription)

	def get_EnvId(self):
		return self.get_body_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_body_params('EnvId', EnvId)

	def get_PkgVersionId(self):
		return self.get_body_params().get('PkgVersionId')

	def set_PkgVersionId(self,PkgVersionId):
		self.add_body_params('PkgVersionId', PkgVersionId)