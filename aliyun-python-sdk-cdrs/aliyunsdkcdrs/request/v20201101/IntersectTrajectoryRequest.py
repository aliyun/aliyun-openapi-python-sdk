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

class IntersectTrajectoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'IntersectTrajectory')
		self.set_method('POST')

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_DeltaDistance(self):
		return self.get_body_params().get('DeltaDistance')

	def set_DeltaDistance(self,DeltaDistance):
		self.add_body_params('DeltaDistance', DeltaDistance)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_DeltaTime(self):
		return self.get_body_params().get('DeltaTime')

	def set_DeltaTime(self,DeltaTime):
		self.add_body_params('DeltaTime', DeltaTime)

	def get_IdList(self):
		return self.get_body_params().get('IdList')

	def set_IdList(self, IdLists):
		for depth1 in range(len(IdLists)):
			if IdLists[depth1].get('IdType') is not None:
				self.add_body_params('IdList.' + str(depth1 + 1) + '.IdType', IdLists[depth1].get('IdType'))
			if IdLists[depth1].get('IdValue') is not None:
				self.add_body_params('IdList.' + str(depth1 + 1) + '.IdValue', IdLists[depth1].get('IdValue'))