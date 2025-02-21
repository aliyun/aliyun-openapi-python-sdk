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
from aliyunsdkbrain_industrial.endpoint import endpoint_data
import json

class CreateEssOptJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'brain-industrial', '2020-09-20', 'CreateEssOptJob','aistudio')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SystemData(self): # Array
		return self.get_body_params().get('SystemData')

	def set_SystemData(self, SystemData):  # Array
		self.add_body_params("SystemData", json.dumps(SystemData))
	def get_TimeZone(self): # String
		return self.get_body_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_body_params('TimeZone', TimeZone)
	def get_ElecPrice(self): # Array
		return self.get_body_params().get('ElecPrice')

	def set_ElecPrice(self, ElecPrice):  # Array
		self.add_body_params("ElecPrice", json.dumps(ElecPrice))
	def get_Freq(self): # String
		return self.get_body_params().get('Freq')

	def set_Freq(self, Freq):  # String
		self.add_body_params('Freq', Freq)
	def get_Duration(self): # Integer
		return self.get_body_params().get('Duration')

	def set_Duration(self, Duration):  # Integer
		self.add_body_params('Duration', Duration)
	def get_RunDate(self): # String
		return self.get_body_params().get('RunDate')

	def set_RunDate(self, RunDate):  # String
		self.add_body_params('RunDate', RunDate)
	def get_TopoType(self): # String
		return self.get_body_params().get('TopoType')

	def set_TopoType(self, TopoType):  # String
		self.add_body_params('TopoType', TopoType)
	def get_GenPrice(self): # Array
		return self.get_body_params().get('GenPrice')

	def set_GenPrice(self, GenPrice):  # Array
		self.add_body_params("GenPrice", json.dumps(GenPrice))
	def get_Location(self): # Struct
		return self.get_body_params().get('Location')

	def set_Location(self, Location):  # Struct
		self.add_body_params("Location", json.dumps(Location))
	def get_ModelVersion(self): # String
		return self.get_body_params().get('ModelVersion')

	def set_ModelVersion(self, ModelVersion):  # String
		self.add_body_params('ModelVersion', ModelVersion)
