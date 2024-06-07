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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateFile')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileType(self): # Integer
		return self.get_body_params().get('FileType')

	def set_FileType(self, FileType):  # Integer
		self.add_body_params('FileType', FileType)
	def get_DependentNodeIdList(self): # String
		return self.get_body_params().get('DependentNodeIdList')

	def set_DependentNodeIdList(self, DependentNodeIdList):  # String
		self.add_body_params('DependentNodeIdList', DependentNodeIdList)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
	def get_ProjectIdentifier(self): # String
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self, ProjectIdentifier):  # String
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)
	def get_ResourceGroupId(self): # Long
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # Long
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_StartImmediately(self): # Boolean
		return self.get_body_params().get('StartImmediately')

	def set_StartImmediately(self, StartImmediately):  # Boolean
		self.add_body_params('StartImmediately', StartImmediately)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_AdvancedSettings(self): # String
		return self.get_body_params().get('AdvancedSettings')

	def set_AdvancedSettings(self, AdvancedSettings):  # String
		self.add_body_params('AdvancedSettings', AdvancedSettings)
	def get_StartEffectDate(self): # Long
		return self.get_body_params().get('StartEffectDate')

	def set_StartEffectDate(self, StartEffectDate):  # Long
		self.add_body_params('StartEffectDate', StartEffectDate)
	def get_CycleType(self): # String
		return self.get_body_params().get('CycleType')

	def set_CycleType(self, CycleType):  # String
		self.add_body_params('CycleType', CycleType)
	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_AutoRerunIntervalMillis(self): # Integer
		return self.get_body_params().get('AutoRerunIntervalMillis')

	def set_AutoRerunIntervalMillis(self, AutoRerunIntervalMillis):  # Integer
		self.add_body_params('AutoRerunIntervalMillis', AutoRerunIntervalMillis)
	def get_InputList(self): # String
		return self.get_body_params().get('InputList')

	def set_InputList(self, InputList):  # String
		self.add_body_params('InputList', InputList)
	def get_CreateFolderIfNotExists(self): # Boolean
		return self.get_body_params().get('CreateFolderIfNotExists')

	def set_CreateFolderIfNotExists(self, CreateFolderIfNotExists):  # Boolean
		self.add_body_params('CreateFolderIfNotExists', CreateFolderIfNotExists)
	def get_RerunMode(self): # String
		return self.get_body_params().get('RerunMode')

	def set_RerunMode(self, RerunMode):  # String
		self.add_body_params('RerunMode', RerunMode)
	def get_ConnectionName(self): # String
		return self.get_body_params().get('ConnectionName')

	def set_ConnectionName(self, ConnectionName):  # String
		self.add_body_params('ConnectionName', ConnectionName)
	def get_OutputParameters(self): # String
		return self.get_body_params().get('OutputParameters')

	def set_OutputParameters(self, OutputParameters):  # String
		self.add_body_params('OutputParameters', OutputParameters)
	def get_ParaValue(self): # String
		return self.get_body_params().get('ParaValue')

	def set_ParaValue(self, ParaValue):  # String
		self.add_body_params('ParaValue', ParaValue)
	def get_ResourceGroupIdentifier(self): # String
		return self.get_body_params().get('ResourceGroupIdentifier')

	def set_ResourceGroupIdentifier(self, ResourceGroupIdentifier):  # String
		self.add_body_params('ResourceGroupIdentifier', ResourceGroupIdentifier)
	def get_AutoRerunTimes(self): # Integer
		return self.get_body_params().get('AutoRerunTimes')

	def set_AutoRerunTimes(self, AutoRerunTimes):  # Integer
		self.add_body_params('AutoRerunTimes', AutoRerunTimes)
	def get_CronExpress(self): # String
		return self.get_body_params().get('CronExpress')

	def set_CronExpress(self, CronExpress):  # String
		self.add_body_params('CronExpress', CronExpress)
	def get_IgnoreParentSkipRunningProperty(self): # Boolean
		return self.get_body_params().get('IgnoreParentSkipRunningProperty')

	def set_IgnoreParentSkipRunningProperty(self, IgnoreParentSkipRunningProperty):  # Boolean
		self.add_body_params('IgnoreParentSkipRunningProperty', IgnoreParentSkipRunningProperty)
	def get_EndEffectDate(self): # Long
		return self.get_body_params().get('EndEffectDate')

	def set_EndEffectDate(self, EndEffectDate):  # Long
		self.add_body_params('EndEffectDate', EndEffectDate)
	def get_FileName(self): # String
		return self.get_body_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_body_params('FileName', FileName)
	def get_InputParameters(self): # String
		return self.get_body_params().get('InputParameters')

	def set_InputParameters(self, InputParameters):  # String
		self.add_body_params('InputParameters', InputParameters)
	def get_Stop(self): # Boolean
		return self.get_body_params().get('Stop')

	def set_Stop(self, Stop):  # Boolean
		self.add_body_params('Stop', Stop)
	def get_DependentType(self): # String
		return self.get_body_params().get('DependentType')

	def set_DependentType(self, DependentType):  # String
		self.add_body_params('DependentType', DependentType)
	def get_FileFolderPath(self): # String
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self, FileFolderPath):  # String
		self.add_body_params('FileFolderPath', FileFolderPath)
	def get_FileDescription(self): # String
		return self.get_body_params().get('FileDescription')

	def set_FileDescription(self, FileDescription):  # String
		self.add_body_params('FileDescription', FileDescription)
	def get_AutoParsing(self): # Boolean
		return self.get_body_params().get('AutoParsing')

	def set_AutoParsing(self, AutoParsing):  # Boolean
		self.add_body_params('AutoParsing', AutoParsing)
	def get_SchedulerType(self): # String
		return self.get_body_params().get('SchedulerType')

	def set_SchedulerType(self, SchedulerType):  # String
		self.add_body_params('SchedulerType', SchedulerType)
