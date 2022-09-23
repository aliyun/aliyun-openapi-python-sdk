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
from aliyunsdkehpc.endpoint import endpoint_data

class SubmitJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SubmitJob')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StderrRedirectPath(self): # String
		return self.get_query_params().get('StderrRedirectPath')

	def set_StderrRedirectPath(self, StderrRedirectPath):  # String
		self.add_query_param('StderrRedirectPath', StderrRedirectPath)
	def get_RunasUserPassword(self): # String
		return self.get_query_params().get('RunasUserPassword')

	def set_RunasUserPassword(self, RunasUserPassword):  # String
		self.add_query_param('RunasUserPassword', RunasUserPassword)
	def get_ClockTime(self): # String
		return self.get_query_params().get('ClockTime')

	def set_ClockTime(self, ClockTime):  # String
		self.add_query_param('ClockTime', ClockTime)
	def get_CommandLine(self): # String
		return self.get_query_params().get('CommandLine')

	def set_CommandLine(self, CommandLine):  # String
		self.add_query_param('CommandLine', CommandLine)
	def get_JobQueue(self): # String
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self, JobQueue):  # String
		self.add_query_param('JobQueue', JobQueue)
	def get_ArrayRequest(self): # String
		return self.get_query_params().get('ArrayRequest')

	def set_ArrayRequest(self, ArrayRequest):  # String
		self.add_query_param('ArrayRequest', ArrayRequest)
	def get_UnzipCmd(self): # String
		return self.get_query_params().get('UnzipCmd')

	def set_UnzipCmd(self, UnzipCmd):  # String
		self.add_query_param('UnzipCmd', UnzipCmd)
	def get_PackagePath(self): # String
		return self.get_query_params().get('PackagePath')

	def set_PackagePath(self, PackagePath):  # String
		self.add_query_param('PackagePath', PackagePath)
	def get_Mem(self): # String
		return self.get_query_params().get('Mem')

	def set_Mem(self, Mem):  # String
		self.add_query_param('Mem', Mem)
	def get_StdoutRedirectPath(self): # String
		return self.get_query_params().get('StdoutRedirectPath')

	def set_StdoutRedirectPath(self, StdoutRedirectPath):  # String
		self.add_query_param('StdoutRedirectPath', StdoutRedirectPath)
	def get_Variables(self): # String
		return self.get_query_params().get('Variables')

	def set_Variables(self, Variables):  # String
		self.add_query_param('Variables', Variables)
	def get_PostCmdLine(self): # String
		return self.get_query_params().get('PostCmdLine')

	def set_PostCmdLine(self, PostCmdLine):  # String
		self.add_query_param('PostCmdLine', PostCmdLine)
	def get_RunasUser(self): # String
		return self.get_query_params().get('RunasUser')

	def set_RunasUser(self, RunasUser):  # String
		self.add_query_param('RunasUser', RunasUser)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ReRunable(self): # Boolean
		return self.get_query_params().get('ReRunable')

	def set_ReRunable(self, ReRunable):  # Boolean
		self.add_query_param('ReRunable', ReRunable)
	def get_Thread(self): # Integer
		return self.get_query_params().get('Thread')

	def set_Thread(self, Thread):  # Integer
		self.add_query_param('Thread', Thread)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_Gpu(self): # Integer
		return self.get_query_params().get('Gpu')

	def set_Gpu(self, Gpu):  # Integer
		self.add_query_param('Gpu', Gpu)
	def get_Node(self): # Integer
		return self.get_query_params().get('Node')

	def set_Node(self, Node):  # Integer
		self.add_query_param('Node', Node)
	def get_Task(self): # Integer
		return self.get_query_params().get('Task')

	def set_Task(self, Task):  # Integer
		self.add_query_param('Task', Task)
	def get_InputFileUrl(self): # String
		return self.get_query_params().get('InputFileUrl')

	def set_InputFileUrl(self, InputFileUrl):  # String
		self.add_query_param('InputFileUrl', InputFileUrl)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ContainerId(self): # String
		return self.get_query_params().get('ContainerId')

	def set_ContainerId(self, ContainerId):  # String
		self.add_query_param('ContainerId', ContainerId)
