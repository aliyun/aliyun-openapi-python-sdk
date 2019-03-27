# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateStreamPredictRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ivision', '2019-03-08', 'CreateStreamPredict','ivision')

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

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_ShowLog(self):
		return self.get_query_params().get('ShowLog')

	def set_ShowLog(self,ShowLog):
		self.add_query_param('ShowLog',ShowLog)

	def get_StreamType(self):
		return self.get_query_params().get('StreamType')

	def set_StreamType(self,StreamType):
		self.add_query_param('StreamType',StreamType)

	def get_StreamId(self):
		return self.get_query_params().get('StreamId')

	def set_StreamId(self,StreamId):
		self.add_query_param('StreamId',StreamId)

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