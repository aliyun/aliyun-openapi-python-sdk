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

class InsertApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertApplication','Edas')
		self.set_uri_pattern('/pop/v5/changeorder/co_create_app')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WebContainer(self): # string
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # string
		self.add_query_param('WebContainer', WebContainer)
	def get_EcuInfo(self): # string
		return self.get_query_params().get('EcuInfo')

	def set_EcuInfo(self, EcuInfo):  # string
		self.add_query_param('EcuInfo', EcuInfo)
	def get_MinHeapSize(self): # integer
		return self.get_query_params().get('MinHeapSize')

	def set_MinHeapSize(self, MinHeapSize):  # integer
		self.add_query_param('MinHeapSize', MinHeapSize)
	def get_BuildPackId(self): # integer
		return self.get_query_params().get('BuildPackId')

	def set_BuildPackId(self, BuildPackId):  # integer
		self.add_query_param('BuildPackId', BuildPackId)
	def get_ComponentIds(self): # string
		return self.get_query_params().get('ComponentIds')

	def set_ComponentIds(self, ComponentIds):  # string
		self.add_query_param('ComponentIds', ComponentIds)
	def get_HealthCheckUrl(self): # string
		return self.get_query_params().get('HealthCheckUrl')

	def set_HealthCheckUrl(self, HealthCheckUrl):  # string
		self.add_query_param('HealthCheckUrl', HealthCheckUrl)
	def get_ReservedPortStr(self): # string
		return self.get_query_params().get('ReservedPortStr')

	def set_ReservedPortStr(self, ReservedPortStr):  # string
		self.add_query_param('ReservedPortStr', ReservedPortStr)
	def get_JvmOptions(self): # string
		return self.get_query_params().get('JvmOptions')

	def set_JvmOptions(self, JvmOptions):  # string
		self.add_query_param('JvmOptions', JvmOptions)
	def get_Description(self): # string
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # string
		self.add_query_param('Description', Description)
	def get_Cpu(self): # integer
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # integer
		self.add_query_param('Cpu', Cpu)
	def get_MaxPermSize(self): # integer
		return self.get_query_params().get('MaxPermSize')

	def set_MaxPermSize(self, MaxPermSize):  # integer
		self.add_query_param('MaxPermSize', MaxPermSize)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
	def get_MaxHeapSize(self): # integer
		return self.get_query_params().get('MaxHeapSize')

	def set_MaxHeapSize(self, MaxHeapSize):  # integer
		self.add_query_param('MaxHeapSize', MaxHeapSize)
	def get_EnablePortCheck(self): # boolean
		return self.get_query_params().get('EnablePortCheck')

	def set_EnablePortCheck(self, EnablePortCheck):  # boolean
		self.add_query_param('EnablePortCheck', EnablePortCheck)
	def get_ApplicationName(self): # string
		return self.get_query_params().get('ApplicationName')

	def set_ApplicationName(self, ApplicationName):  # string
		self.add_query_param('ApplicationName', ApplicationName)
	def get_Jdk(self): # string
		return self.get_query_params().get('Jdk')

	def set_Jdk(self, Jdk):  # string
		self.add_query_param('Jdk', Jdk)
	def get_ResourceGroupId(self): # string
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # string
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Mem(self): # integer
		return self.get_query_params().get('Mem')

	def set_Mem(self, Mem):  # integer
		self.add_query_param('Mem', Mem)
	def get_LogicalRegionId(self): # string
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self, LogicalRegionId):  # string
		self.add_query_param('LogicalRegionId', LogicalRegionId)
	def get_EnableUrlCheck(self): # boolean
		return self.get_query_params().get('EnableUrlCheck')

	def set_EnableUrlCheck(self, EnableUrlCheck):  # boolean
		self.add_query_param('EnableUrlCheck', EnableUrlCheck)
	def get_PackageType(self): # string
		return self.get_query_params().get('PackageType')

	def set_PackageType(self, PackageType):  # string
		self.add_query_param('PackageType', PackageType)
	def get_Hooks(self): # string
		return self.get_query_params().get('Hooks')

	def set_Hooks(self, Hooks):  # string
		self.add_query_param('Hooks', Hooks)
