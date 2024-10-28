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
from aliyunsdknas.endpoint import endpoint_data

class CreateDataFlowSubTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateDataFlowSubTask','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DataFlowTaskId(self): # String
		return self.get_query_params().get('DataFlowTaskId')

	def set_DataFlowTaskId(self, DataFlowTaskId):  # String
		self.add_query_param('DataFlowTaskId', DataFlowTaskId)
	def get_SrcFilePath(self): # String
		return self.get_query_params().get('SrcFilePath')

	def set_SrcFilePath(self, SrcFilePath):  # String
		self.add_query_param('SrcFilePath', SrcFilePath)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_DataFlowId(self): # String
		return self.get_query_params().get('DataFlowId')

	def set_DataFlowId(self, DataFlowId):  # String
		self.add_query_param('DataFlowId', DataFlowId)
	def get_DstFilePath(self): # String
		return self.get_query_params().get('DstFilePath')

	def set_DstFilePath(self, DstFilePath):  # String
		self.add_query_param('DstFilePath', DstFilePath)
	def get_Condition(self): # Struct
		return self.get_query_params().get('Condition')

	def set_Condition(self, Condition):  # Struct
		if Condition.get('Size') is not None:
			self.add_query_param('Condition.Size', Condition.get('Size'))
		if Condition.get('ModifyTime') is not None:
			self.add_query_param('Condition.ModifyTime', Condition.get('ModifyTime'))
