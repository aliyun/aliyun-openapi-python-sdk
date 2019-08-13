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
from aliyunsdkemr.endpoint import endpoint_data

class RunETLJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'RunETLJob','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_InstanceRunParams(self):
		return self.get_query_params().get('InstanceRunParams')

	def set_InstanceRunParams(self,InstanceRunParams):
		for i in range(len(InstanceRunParams)):	
			if InstanceRunParams[i].get('Value') is not None:
				self.add_query_param('InstanceRunParam.' + str(i + 1) + '.Value' , InstanceRunParams[i].get('Value'))
			if InstanceRunParams[i].get('Key') is not None:
				self.add_query_param('InstanceRunParam.' + str(i + 1) + '.Key' , InstanceRunParams[i].get('Key'))


	def get_IsDebug(self):
		return self.get_query_params().get('IsDebug')

	def set_IsDebug(self,IsDebug):
		self.add_query_param('IsDebug',IsDebug)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)