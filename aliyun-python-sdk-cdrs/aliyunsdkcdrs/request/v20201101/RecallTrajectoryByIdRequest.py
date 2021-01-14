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

class RecallTrajectoryByIdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'RecallTrajectoryById')
		self.set_method('POST')

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_IdValue(self):
		return self.get_body_params().get('IdValue')

	def set_IdValue(self,IdValue):
		self.add_body_params('IdValue', IdValue)

	def get_DeltaDistance(self):
		return self.get_body_params().get('DeltaDistance')

	def set_DeltaDistance(self,DeltaDistance):
		self.add_body_params('DeltaDistance', DeltaDistance)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_IdType(self):
		return self.get_body_params().get('IdType')

	def set_IdType(self,IdType):
		self.add_body_params('IdType', IdType)

	def get_OutputIdTypeList(self):
		return self.get_body_params().get('OutputIdTypeList')

	def set_OutputIdTypeList(self, OutputIdTypeLists):
		for depth1 in range(len(OutputIdTypeLists)):
			if OutputIdTypeLists[depth1] is not None:
				self.add_body_params('OutputIdTypeList.' + str(depth1 + 1) , OutputIdTypeLists[depth1])

	def get_DeltaTime(self):
		return self.get_body_params().get('DeltaTime')

	def set_DeltaTime(self,DeltaTime):
		self.add_body_params('DeltaTime', DeltaTime)

	def get_OutputIdCount(self):
		return self.get_body_params().get('OutputIdCount')

	def set_OutputIdCount(self,OutputIdCount):
		self.add_body_params('OutputIdCount', OutputIdCount)