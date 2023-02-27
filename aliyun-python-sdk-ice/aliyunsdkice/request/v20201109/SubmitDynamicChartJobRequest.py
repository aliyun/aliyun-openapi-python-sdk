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
from aliyunsdkice.endpoint import endpoint_data

class SubmitDynamicChartJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitDynamicChartJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OutputConfig(self): # String
		return self.get_query_params().get('OutputConfig')

	def set_OutputConfig(self, OutputConfig):  # String
		self.add_query_param('OutputConfig', OutputConfig)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_ChartType(self): # String
		return self.get_query_params().get('ChartType')

	def set_ChartType(self, ChartType):  # String
		self.add_query_param('ChartType', ChartType)
	def get_ChartTitle(self): # String
		return self.get_query_params().get('ChartTitle')

	def set_ChartTitle(self, ChartTitle):  # String
		self.add_query_param('ChartTitle', ChartTitle)
	def get_ChartConfig(self): # String
		return self.get_query_params().get('ChartConfig')

	def set_ChartConfig(self, ChartConfig):  # String
		self.add_query_param('ChartConfig', ChartConfig)
	def get_Input(self): # String
		return self.get_query_params().get('Input')

	def set_Input(self, Input):  # String
		self.add_query_param('Input', Input)
	def get_Unit(self): # String
		return self.get_query_params().get('Unit')

	def set_Unit(self, Unit):  # String
		self.add_query_param('Unit', Unit)
	def get_DataSource(self): # String
		return self.get_query_params().get('DataSource')

	def set_DataSource(self, DataSource):  # String
		self.add_query_param('DataSource', DataSource)
	def get_Background(self): # String
		return self.get_query_params().get('Background')

	def set_Background(self, Background):  # String
		self.add_query_param('Background', Background)
	def get_Subtitle(self): # String
		return self.get_query_params().get('Subtitle')

	def set_Subtitle(self, Subtitle):  # String
		self.add_query_param('Subtitle', Subtitle)
	def get_AxisParams(self): # String
		return self.get_query_params().get('AxisParams')

	def set_AxisParams(self, AxisParams):  # String
		self.add_query_param('AxisParams', AxisParams)
