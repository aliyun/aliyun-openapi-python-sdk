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
from aliyunsdksls.endpoint import endpoint_data

class CreateImportIngestionJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sls', '2019-10-23', 'CreateImportIngestionJob')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Args(self):
		return self.get_body_params().get('Args')

	def set_Args(self,Args):
		self.add_body_params('Args', Args)

	def get_Image(self):
		return self.get_body_params().get('Image')

	def set_Image(self,Image):
		self.add_body_params('Image', Image)

	def get_EnvFromSecret(self):
		return self.get_body_params().get('EnvFromSecret')

	def set_EnvFromSecret(self,EnvFromSecret):
		self.add_body_params('EnvFromSecret', EnvFromSecret)

	def get_RestartPolicy(self):
		return self.get_body_params().get('RestartPolicy')

	def set_RestartPolicy(self,RestartPolicy):
		self.add_body_params('RestartPolicy', RestartPolicy)

	def get_Parallelism(self):
		return self.get_body_params().get('Parallelism')

	def set_Parallelism(self,Parallelism):
		self.add_body_params('Parallelism', Parallelism)

	def get_Namespace(self):
		return self.get_body_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_body_params('Namespace', Namespace)

	def get_Completions(self):
		return self.get_body_params().get('Completions')

	def set_Completions(self,Completions):
		self.add_body_params('Completions', Completions)

	def get_EnvVars(self):
		return self.get_body_params().get('EnvVars')

	def set_EnvVars(self,EnvVars):
		self.add_body_params('EnvVars', EnvVars)

	def get_ImagePullSecret(self):
		return self.get_body_params().get('ImagePullSecret')

	def set_ImagePullSecret(self,ImagePullSecret):
		self.add_body_params('ImagePullSecret', ImagePullSecret)

	def get_CallerId(self):
		return self.get_body_params().get('CallerId')

	def set_CallerId(self,CallerId):
		self.add_body_params('CallerId', CallerId)

	def get_Region(self):
		return self.get_body_params().get('Region')

	def set_Region(self,Region):
		self.add_body_params('Region', Region)

	def get_JobName(self):
		return self.get_body_params().get('JobName')

	def set_JobName(self,JobName):
		self.add_body_params('JobName', JobName)