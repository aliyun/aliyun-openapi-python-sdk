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

class RunApplicationActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'RunApplicationAction','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ExecuteStrategy(self):
		return self.get_query_params().get('ExecuteStrategy')

	def set_ExecuteStrategy(self,ExecuteStrategy):
		self.add_query_param('ExecuteStrategy',ExecuteStrategy)

	def get_NodeCountPerBatch(self):
		return self.get_query_params().get('NodeCountPerBatch')

	def set_NodeCountPerBatch(self,NodeCountPerBatch):
		self.add_query_param('NodeCountPerBatch',NodeCountPerBatch)

	def get_ComponentInstanceSelector(self):
		return self.get_query_params().get('ComponentInstanceSelector')

	def set_ComponentInstanceSelector(self,ComponentInstanceSelector):
		self.add_query_param('ComponentInstanceSelector',ComponentInstanceSelector)

	def get_RollingExecute(self):
		return self.get_query_params().get('RollingExecute')

	def set_RollingExecute(self,RollingExecute):
		self.add_query_param('RollingExecute',RollingExecute)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ActionName(self):
		return self.get_query_params().get('ActionName')

	def set_ActionName(self,ActionName):
		self.add_query_param('ActionName',ActionName)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_CustomParams(self):
		return self.get_query_params().get('CustomParams')

	def set_CustomParams(self,CustomParams):
		self.add_query_param('CustomParams',CustomParams)