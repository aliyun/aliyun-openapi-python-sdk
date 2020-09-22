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
from aliyunsdkivision.endpoint import endpoint_data

class CreateStreamPredictRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ivision', '2019-03-08', 'CreateStreamPredict','ivision')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_AutoStart(self):
		return self.get_query_params().get('AutoStart')

	def set_AutoStart(self,AutoStart):
		self.add_query_param('AutoStart',AutoStart)

	def get_Notify(self):
		return self.get_query_params().get('Notify')

	def set_Notify(self,Notify):
		self.add_query_param('Notify',Notify)

	def get_Output(self):
		return self.get_query_params().get('Output')

	def set_Output(self,Output):
		self.add_query_param('Output',Output)

	def get_StreamType(self):
		return self.get_query_params().get('StreamType')

	def set_StreamType(self,StreamType):
		self.add_query_param('StreamType',StreamType)

	def get_FaceGroupId(self):
		return self.get_query_params().get('FaceGroupId')

	def set_FaceGroupId(self,FaceGroupId):
		self.add_query_param('FaceGroupId',FaceGroupId)

	def get_StreamId(self):
		return self.get_query_params().get('StreamId')

	def set_StreamId(self,StreamId):
		self.add_query_param('StreamId',StreamId)

	def get_PredictTemplateId(self):
		return self.get_query_params().get('PredictTemplateId')

	def set_PredictTemplateId(self,PredictTemplateId):
		self.add_query_param('PredictTemplateId',PredictTemplateId)

	def get_DetectIntervals(self):
		return self.get_query_params().get('DetectIntervals')

	def set_DetectIntervals(self,DetectIntervals):
		self.add_query_param('DetectIntervals',DetectIntervals)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ProbabilityThresholds(self):
		return self.get_query_params().get('ProbabilityThresholds')

	def set_ProbabilityThresholds(self,ProbabilityThresholds):
		self.add_query_param('ProbabilityThresholds',ProbabilityThresholds)

	def get_ModelIds(self):
		return self.get_query_params().get('ModelIds')

	def set_ModelIds(self,ModelIds):
		self.add_query_param('ModelIds',ModelIds)

	def get_ModelUserData(self):
		return self.get_query_params().get('ModelUserData')

	def set_ModelUserData(self,ModelUserData):
		self.add_query_param('ModelUserData',ModelUserData)