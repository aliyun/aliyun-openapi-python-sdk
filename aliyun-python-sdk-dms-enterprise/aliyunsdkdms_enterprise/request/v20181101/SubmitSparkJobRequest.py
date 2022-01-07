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
from aliyunsdkdms_enterprise.endpoint import endpoint_data
import json

class SubmitSparkJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'SubmitSparkJob','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MainClass(self): # String
		return self.get_body_params().get('MainClass')

	def set_MainClass(self, MainClass):  # String
		self.add_body_params('MainClass', MainClass)
	def get_Configuration(self): # Map
		return self.get_body_params().get('Configuration')

	def set_Configuration(self, Configuration):  # Map
		self.add_body_params("Configuration", json.dumps(Configuration))
	def get_OssInfo(self): # Struct
		return self.get_body_params().get('OssInfo')

	def set_OssInfo(self, OssInfo):  # Struct
		self.add_body_params("OssInfo", json.dumps(OssInfo))
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_MainFile(self): # String
		return self.get_body_params().get('MainFile')

	def set_MainFile(self, MainFile):  # String
		self.add_body_params('MainFile', MainFile)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Files(self): # Array
		return self.get_body_params().get('Files')

	def set_Files(self, Files):  # Array
		self.add_body_params("Files", json.dumps(Files))
	def get_AppCode(self): # String
		return self.get_body_params().get('AppCode')

	def set_AppCode(self, AppCode):  # String
		self.add_body_params('AppCode', AppCode)
	def get_Arguments(self): # Array
		return self.get_body_params().get('Arguments')

	def set_Arguments(self, Arguments):  # Array
		self.add_body_params("Arguments", json.dumps(Arguments))
