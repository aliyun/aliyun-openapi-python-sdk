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
from aliyunsdkimm.endpoint import endpoint_data
import json

class CreateFigureClustersMergingTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateFigureClustersMergingTask','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_Notification(self): # Struct
		return self.get_query_params().get('Notification')

	def set_Notification(self, Notification):  # Struct
		self.add_query_param("Notification", json.dumps(Notification))
	def get_DatasetName(self): # String
		return self.get_query_params().get('DatasetName')

	def set_DatasetName(self, DatasetName):  # String
		self.add_query_param('DatasetName', DatasetName)
	def get_From(self): # String
		return self.get_query_params().get('From')

	def set_From(self, _From):  # String
		self.add_query_param('From', _From)
	def get_Froms(self): # Array
		return self.get_query_params().get('Froms')

	def set_Froms(self, Froms):  # Array
		self.add_query_param("Froms", json.dumps(Froms))
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_To(self): # String
		return self.get_query_params().get('To')

	def set_To(self, To):  # String
		self.add_query_param('To', To)
