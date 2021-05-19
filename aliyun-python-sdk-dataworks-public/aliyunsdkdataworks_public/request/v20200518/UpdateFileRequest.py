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

class UpdateFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateFile')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OutputList(self):
		return self.get_body_params().get('OutputList')

	def set_OutputList(self,OutputList):
		self.add_body_params('OutputList', OutputList)

	def get_DependentNodeIdList(self):
		return self.get_body_params().get('DependentNodeIdList')

	def set_DependentNodeIdList(self,DependentNodeIdList):
		self.add_body_params('DependentNodeIdList', DependentNodeIdList)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_ProjectIdentifier(self):
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self,ProjectIdentifier):
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_StartEffectDate(self):
		return self.get_body_params().get('StartEffectDate')

	def set_StartEffectDate(self,StartEffectDate):
		self.add_body_params('StartEffectDate', StartEffectDate)

	def get_CycleType(self):
		return self.get_body_params().get('CycleType')

	def set_CycleType(self,CycleType):
		self.add_body_params('CycleType', CycleType)

	def get_FileId(self):
		return self.get_body_params().get('FileId')

	def set_FileId(self,FileId):
		self.add_body_params('FileId', FileId)

	def get_AutoRerunIntervalMillis(self):
		return self.get_body_params().get('AutoRerunIntervalMillis')

	def set_AutoRerunIntervalMillis(self,AutoRerunIntervalMillis):
		self.add_body_params('AutoRerunIntervalMillis', AutoRerunIntervalMillis)

	def get_Owner(self):
		return self.get_body_params().get('Owner')

	def set_Owner(self,Owner):
		self.add_body_params('Owner', Owner)

	def get_InputList(self):
		return self.get_body_params().get('InputList')

	def set_InputList(self,InputList):
		self.add_body_params('InputList', InputList)

	def get_RerunMode(self):
		return self.get_body_params().get('RerunMode')

	def set_RerunMode(self,RerunMode):
		self.add_body_params('RerunMode', RerunMode)

	def get_ConnectionName(self):
		return self.get_body_params().get('ConnectionName')

	def set_ConnectionName(self,ConnectionName):
		self.add_body_params('ConnectionName', ConnectionName)

	def get_ParaValue(self):
		return self.get_body_params().get('ParaValue')

	def set_ParaValue(self,ParaValue):
		self.add_body_params('ParaValue', ParaValue)

	def get_ResourceGroupIdentifier(self):
		return self.get_body_params().get('ResourceGroupIdentifier')

	def set_ResourceGroupIdentifier(self,ResourceGroupIdentifier):
		self.add_body_params('ResourceGroupIdentifier', ResourceGroupIdentifier)

	def get_AutoRerunTimes(self):
		return self.get_body_params().get('AutoRerunTimes')

	def set_AutoRerunTimes(self,AutoRerunTimes):
		self.add_body_params('AutoRerunTimes', AutoRerunTimes)

	def get_CronExpress(self):
		return self.get_body_params().get('CronExpress')

	def set_CronExpress(self,CronExpress):
		self.add_body_params('CronExpress', CronExpress)

	def get_EndEffectDate(self):
		return self.get_body_params().get('EndEffectDate')

	def set_EndEffectDate(self,EndEffectDate):
		self.add_body_params('EndEffectDate', EndEffectDate)

	def get_FileName(self):
		return self.get_body_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_body_params('FileName', FileName)

	def get_Stop(self):
		return self.get_body_params().get('Stop')

	def set_Stop(self,Stop):
		self.add_body_params('Stop', Stop)

	def get_DependentType(self):
		return self.get_body_params().get('DependentType')

	def set_DependentType(self,DependentType):
		self.add_body_params('DependentType', DependentType)

	def get_FileFolderPath(self):
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self,FileFolderPath):
		self.add_body_params('FileFolderPath', FileFolderPath)

	def get_FileDescription(self):
		return self.get_body_params().get('FileDescription')

	def set_FileDescription(self,FileDescription):
		self.add_body_params('FileDescription', FileDescription)

	def get_AutoParsing(self):
		return self.get_body_params().get('AutoParsing')

	def set_AutoParsing(self,AutoParsing):
		self.add_body_params('AutoParsing', AutoParsing)