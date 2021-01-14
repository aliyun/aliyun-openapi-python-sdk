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

class DetectTrajectoryRegularPatternRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'DetectTrajectoryRegularPattern')
		self.set_method('POST')

	def get_PredictDate(self):
		return self.get_body_params().get('PredictDate')

	def set_PredictDate(self,PredictDate):
		self.add_body_params('PredictDate', PredictDate)

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_IdValue(self):
		return self.get_body_params().get('IdValue')

	def set_IdValue(self,IdValue):
		self.add_body_params('IdValue', IdValue)

	def get_IdType(self):
		return self.get_body_params().get('IdType')

	def set_IdType(self,IdType):
		self.add_body_params('IdType', IdType)