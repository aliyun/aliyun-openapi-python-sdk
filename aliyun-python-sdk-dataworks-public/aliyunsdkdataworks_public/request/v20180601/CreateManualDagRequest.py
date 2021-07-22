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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateManualDagRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2018-06-01', 'CreateManualDag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectName(self):
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_query_param('ProjectName',ProjectName)

	def get_Bizdate(self):
		return self.get_query_params().get('Bizdate')

	def set_Bizdate(self,Bizdate):
		self.add_query_param('Bizdate',Bizdate)

	def get_FlowName(self):
		return self.get_query_params().get('FlowName')

	def set_FlowName(self,FlowName):
		self.add_query_param('FlowName',FlowName)

	def get_DagPara(self):
		return self.get_query_params().get('DagPara')

	def set_DagPara(self,DagPara):
		self.add_query_param('DagPara',DagPara)

	def get_NodePara(self):
		return self.get_query_params().get('NodePara')

	def set_NodePara(self,NodePara):
		self.add_query_param('NodePara',NodePara)