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
from aliyunsdkgpdb.endpoint import endpoint_data

class CreateStreamingDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateStreamingDataSource','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataSourceType(self): # String
		return self.get_query_params().get('DataSourceType')

	def set_DataSourceType(self, DataSourceType):  # String
		self.add_query_param('DataSourceType', DataSourceType)
	def get_DataSourceDescription(self): # String
		return self.get_query_params().get('DataSourceDescription')

	def set_DataSourceDescription(self, DataSourceDescription):  # String
		self.add_query_param('DataSourceDescription', DataSourceDescription)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DataSourceName(self): # String
		return self.get_query_params().get('DataSourceName')

	def set_DataSourceName(self, DataSourceName):  # String
		self.add_query_param('DataSourceName', DataSourceName)
	def get_DataSourceConfig(self): # String
		return self.get_query_params().get('DataSourceConfig')

	def set_DataSourceConfig(self, DataSourceConfig):  # String
		self.add_query_param('DataSourceConfig', DataSourceConfig)
	def get_ServiceId(self): # Integer
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # Integer
		self.add_query_param('ServiceId', ServiceId)
