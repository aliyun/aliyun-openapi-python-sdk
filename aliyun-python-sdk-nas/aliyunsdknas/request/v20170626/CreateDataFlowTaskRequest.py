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

class CreateDataFlowTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateDataFlowTask','nas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Directory(self):
		return self.get_query_params().get('Directory')

	def set_Directory(self,Directory):
		self.add_query_param('Directory',Directory)

	def get_SrcTaskId(self):
		return self.get_query_params().get('SrcTaskId')

	def set_SrcTaskId(self,SrcTaskId):
		self.add_query_param('SrcTaskId',SrcTaskId)

	def get_DataType(self):
		return self.get_query_params().get('DataType')

	def set_DataType(self,DataType):
		self.add_query_param('DataType',DataType)

	def get_FileSystemId(self):
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self,FileSystemId):
		self.add_query_param('FileSystemId',FileSystemId)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_DataFlowId(self):
		return self.get_query_params().get('DataFlowId')

	def set_DataFlowId(self,DataFlowId):
		self.add_query_param('DataFlowId',DataFlowId)

	def get_EntryList(self):
		return self.get_query_params().get('EntryList')

	def set_EntryList(self,EntryList):
		self.add_query_param('EntryList',EntryList)

	def get_TaskAction(self):
		return self.get_query_params().get('TaskAction')

	def set_TaskAction(self,TaskAction):
		self.add_query_param('TaskAction',TaskAction)