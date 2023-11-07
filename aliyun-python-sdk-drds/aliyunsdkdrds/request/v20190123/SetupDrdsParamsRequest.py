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
from aliyunsdkdrds.endpoint import endpoint_data

class SetupDrdsParamsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SetupDrdsParams','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ParamLevel(self): # String
		return self.get_query_params().get('ParamLevel')

	def set_ParamLevel(self, ParamLevel):  # String
		self.add_query_param('ParamLevel', ParamLevel)
	def get_Datas(self): # RepeatList
		return self.get_query_params().get('Data')

	def set_Datas(self, Data):  # RepeatList
		for depth1 in range(len(Data)):
			if Data[depth1].get('ParamType') is not None:
				self.add_query_param('Data.' + str(depth1 + 1) + '.ParamType', Data[depth1].get('ParamType'))
			if Data[depth1].get('DbName') is not None:
				self.add_query_param('Data.' + str(depth1 + 1) + '.DbName', Data[depth1].get('DbName'))
			if Data[depth1].get('ParamRanges') is not None:
				self.add_query_param('Data.' + str(depth1 + 1) + '.ParamRanges', Data[depth1].get('ParamRanges'))
			if Data[depth1].get('ParamVariableName') is not None:
				self.add_query_param('Data.' + str(depth1 + 1) + '.ParamVariableName', Data[depth1].get('ParamVariableName'))
			if Data[depth1].get('ParamValue') is not None:
				self.add_query_param('Data.' + str(depth1 + 1) + '.ParamValue', Data[depth1].get('ParamValue'))
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
