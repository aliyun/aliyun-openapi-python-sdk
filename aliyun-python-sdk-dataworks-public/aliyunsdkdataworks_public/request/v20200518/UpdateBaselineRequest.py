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
import json

class UpdateBaselineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateBaseline')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_RemoveNodeIds(self): # String
		return self.get_body_params().get('RemoveNodeIds')

	def set_RemoveNodeIds(self, RemoveNodeIds):  # String
		self.add_body_params('RemoveNodeIds', RemoveNodeIds)
	def get_AlertMarginThreshold(self): # Integer
		return self.get_body_params().get('AlertMarginThreshold')

	def set_AlertMarginThreshold(self, AlertMarginThreshold):  # Integer
		self.add_body_params('AlertMarginThreshold', AlertMarginThreshold)
	def get_OvertimeSettings(self): # Array
		return self.get_body_params().get('OvertimeSettings')

	def set_OvertimeSettings(self, OvertimeSettings):  # Array
		self.add_body_params("OvertimeSettings", json.dumps(OvertimeSettings))
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_BaselineId(self): # Long
		return self.get_body_params().get('BaselineId')

	def set_BaselineId(self, BaselineId):  # Long
		self.add_body_params('BaselineId', BaselineId)
	def get_Enabled(self): # Boolean
		return self.get_body_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Boolean
		self.add_body_params('Enabled', Enabled)
	def get_BaselineType(self): # String
		return self.get_body_params().get('BaselineType')

	def set_BaselineType(self, BaselineType):  # String
		self.add_body_params('BaselineType', BaselineType)
	def get_AlertEnabled(self): # Boolean
		return self.get_body_params().get('AlertEnabled')

	def set_AlertEnabled(self, AlertEnabled):  # Boolean
		self.add_body_params('AlertEnabled', AlertEnabled)
	def get_AlertSettings(self): # Array
		return self.get_body_params().get('AlertSettings')

	def set_AlertSettings(self, AlertSettings):  # Array
		self.add_body_params("AlertSettings", json.dumps(AlertSettings))
	def get_BaselineName(self): # String
		return self.get_body_params().get('BaselineName')

	def set_BaselineName(self, BaselineName):  # String
		self.add_body_params('BaselineName', BaselineName)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_NodeIds(self): # String
		return self.get_body_params().get('NodeIds')

	def set_NodeIds(self, NodeIds):  # String
		self.add_body_params('NodeIds', NodeIds)
