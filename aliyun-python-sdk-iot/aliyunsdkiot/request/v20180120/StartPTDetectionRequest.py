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
from aliyunsdkiot.endpoint import endpoint_data

class StartPTDetectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'StartPTDetection','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PowerStationUid(self):
		return self.get_query_params().get('PowerStationUid')

	def set_PowerStationUid(self,PowerStationUid):
		self.add_query_param('PowerStationUid',PowerStationUid)

	def get_Data(self):
		return self.get_query_params().get('Data')

	def set_Data(self,Data):
		self.add_query_param('Data',Data)

	def get_PowerPlantsNumber(self):
		return self.get_query_params().get('PowerPlantsNumber')

	def set_PowerPlantsNumber(self,PowerPlantsNumber):
		self.add_query_param('PowerPlantsNumber',PowerPlantsNumber)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_AlgorithmInstanceUid(self):
		return self.get_query_params().get('AlgorithmInstanceUid')

	def set_AlgorithmInstanceUid(self,AlgorithmInstanceUid):
		self.add_query_param('AlgorithmInstanceUid',AlgorithmInstanceUid)

	def get_FileName(self):
		return self.get_query_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_query_param('FileName',FileName)

	def get_DataCollectionTime(self):
		return self.get_query_params().get('DataCollectionTime')

	def set_DataCollectionTime(self,DataCollectionTime):
		self.add_query_param('DataCollectionTime',DataCollectionTime)

	def get_Sensitivity(self):
		return self.get_query_params().get('Sensitivity')

	def set_Sensitivity(self,Sensitivity):
		self.add_query_param('Sensitivity',Sensitivity)