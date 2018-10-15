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
class CreateApiStageVariableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateApiStageVariable','apigateway')

	def get_SupportRoute(self):
		return self.get_query_params().get('SupportRoute')

	def set_SupportRoute(self,SupportRoute):
		self.add_query_param('SupportRoute',SupportRoute)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_VariableName(self):
		return self.get_query_params().get('VariableName')

	def set_VariableName(self,VariableName):
		self.add_query_param('VariableName',VariableName)

	def get_VariableValue(self):
		return self.get_query_params().get('VariableValue')

	def set_VariableValue(self,VariableValue):
		self.add_query_param('VariableValue',VariableValue)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_StageRouteModel(self):
		return self.get_query_params().get('StageRouteModel')

	def set_StageRouteModel(self,StageRouteModel):
		self.add_query_param('StageRouteModel',StageRouteModel)

	def get_StageId(self):
		return self.get_query_params().get('StageId')

	def set_StageId(self,StageId):
		self.add_query_param('StageId',StageId)