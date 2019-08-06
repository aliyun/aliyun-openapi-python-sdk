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

class SetupDrdsParamsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SetupDrdsParams','drds')

	def get_ParamLevel(self):
		return self.get_query_params().get('ParamLevel')

	def set_ParamLevel(self,ParamLevel):
		self.add_query_param('ParamLevel',ParamLevel)

	def get_Datas(self):
		return self.get_query_params().get('Datas')

	def set_Datas(self,Datas):
		for i in range(len(Datas)):	
			if Datas[i].get('ParamType') is not None:
				self.add_query_param('Data.' + str(i + 1) + '.ParamType' , Datas[i].get('ParamType'))
			if Datas[i].get('DbName') is not None:
				self.add_query_param('Data.' + str(i + 1) + '.DbName' , Datas[i].get('DbName'))
			if Datas[i].get('ParamRanges') is not None:
				self.add_query_param('Data.' + str(i + 1) + '.ParamRanges' , Datas[i].get('ParamRanges'))
			if Datas[i].get('ParamVariableName') is not None:
				self.add_query_param('Data.' + str(i + 1) + '.ParamVariableName' , Datas[i].get('ParamVariableName'))
			if Datas[i].get('ParamValue') is not None:
				self.add_query_param('Data.' + str(i + 1) + '.ParamValue' , Datas[i].get('ParamValue'))


	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)