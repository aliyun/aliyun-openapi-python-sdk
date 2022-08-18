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

class StartK8sAppPrecheckRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'StartK8sAppPrecheck','Edas')
		self.set_uri_pattern('/pop/v5/k8s/app_precheck')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Replicas(self): # integer
		return self.get_query_params().get('Replicas')

	def set_Replicas(self, Replicas):  # integer
		self.add_query_param('Replicas', Replicas)
	def get_RequestsEphemeralStorage(self): # integer
		return self.get_query_params().get('RequestsEphemeralStorage')

	def set_RequestsEphemeralStorage(self, RequestsEphemeralStorage):  # integer
		self.add_query_param('RequestsEphemeralStorage', RequestsEphemeralStorage)
	def get_Envs(self): # string
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # string
		self.add_query_param('Envs', Envs)
	def get_Annotations(self): # string
		return self.get_query_params().get('Annotations')

	def set_Annotations(self, Annotations):  # string
		self.add_query_param('Annotations', Annotations)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
	def get_RequestsMem(self): # integer
		return self.get_query_params().get('RequestsMem')

	def set_RequestsMem(self, RequestsMem):  # integer
		self.add_query_param('RequestsMem', RequestsMem)
	def get_LocalVolume(self): # string
		return self.get_query_params().get('LocalVolume')

	def set_LocalVolume(self, LocalVolume):  # string
		self.add_query_param('LocalVolume', LocalVolume)
	def get_EnvFroms(self): # string
		return self.get_query_params().get('EnvFroms')

	def set_EnvFroms(self, EnvFroms):  # string
		self.add_query_param('EnvFroms', EnvFroms)
	def get_Labels(self): # string
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # string
		self.add_query_param('Labels', Labels)
	def get_LimitMem(self): # integer
		return self.get_query_params().get('LimitMem')

	def set_LimitMem(self, LimitMem):  # integer
		self.add_query_param('LimitMem', LimitMem)
	def get_LimitEphemeralStorage(self): # integer
		return self.get_query_params().get('LimitEphemeralStorage')

	def set_LimitEphemeralStorage(self, LimitEphemeralStorage):  # integer
		self.add_query_param('LimitEphemeralStorage', LimitEphemeralStorage)
	def get_LimitmCpu(self): # integer
		return self.get_query_params().get('LimitmCpu')

	def set_LimitmCpu(self, LimitmCpu):  # integer
		self.add_query_param('LimitmCpu', LimitmCpu)
	def get_ConfigMountDescs(self): # string
		return self.get_query_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self, ConfigMountDescs):  # string
		self.add_query_param('ConfigMountDescs', ConfigMountDescs)
	def get_AppName(self): # string
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # string
		self.add_query_param('AppName', AppName)
	def get_PackageUrl(self): # string
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # string
		self.add_query_param('PackageUrl', PackageUrl)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_EmptyDirs(self): # string
		return self.get_query_params().get('EmptyDirs')

	def set_EmptyDirs(self, EmptyDirs):  # string
		self.add_query_param('EmptyDirs', EmptyDirs)
	def get_PvcMountDescs(self): # string
		return self.get_query_params().get('PvcMountDescs')

	def set_PvcMountDescs(self, PvcMountDescs):  # string
		self.add_query_param('PvcMountDescs', PvcMountDescs)
	def get_ImageUrl(self): # string
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # string
		self.add_query_param('ImageUrl', ImageUrl)
	def get_Namespace(self): # string
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # string
		self.add_query_param('Namespace', Namespace)
	def get_RequestsmCpu(self): # integer
		return self.get_query_params().get('RequestsmCpu')

	def set_RequestsmCpu(self, RequestsmCpu):  # integer
		self.add_query_param('RequestsmCpu', RequestsmCpu)
	def get_JavaStartUpConfig(self): # string
		return self.get_query_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self, JavaStartUpConfig):  # string
		self.add_query_param('JavaStartUpConfig', JavaStartUpConfig)
