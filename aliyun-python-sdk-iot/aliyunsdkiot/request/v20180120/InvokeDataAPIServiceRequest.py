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
class InvokeDataAPIServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'InvokeDataAPIService','iot')

	def get_ApiSrn(self):
		return self.get_query_params().get('ApiSrn')

	def set_ApiSrn(self,ApiSrn):
		self.add_query_param('ApiSrn',ApiSrn)

	def get_Params(self):
		return self.get_body_params().get('Params')

	def set_Params(self,Params):
		for i in range(len(Params)):	
			if Params[i].get('ListParamType') is not None:
				self.add_body_params('Param.' + str(i + 1) + '.ListParamType' , Params[i].get('ListParamType'))
			for j in range(len(Params[i].get('ListParamValues'))):
				if Params[i].get('ListParamValues')[j] is not None:
					self.add_body_params('Param.' + str(i + 1) + '.ListParamValue.'+str(j + 1), Params[i].get('ListParamValues')[j])
			if Params[i].get('ParamValue') is not None:
				self.add_body_params('Param.' + str(i + 1) + '.ParamValue' , Params[i].get('ParamValue'))
			if Params[i].get('ParamName') is not None:
				self.add_body_params('Param.' + str(i + 1) + '.ParamName' , Params[i].get('ParamName'))
