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

from aliyunsdkcore.request import RoaRequest

class GetDatasourceTableRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'PaiFeatureStore', '2023-06-21', 'GetDatasourceTable')
		self.set_uri_pattern('/api/v1/instances/[InstanceId]/datasources/[DatasourceId]/tables/[TableName]')
		self.set_method('GET')

	def get_InstanceId(self): # String
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_path_param('InstanceId', InstanceId)
	def get_DatasourceId(self): # String
		return self.get_path_params().get('DatasourceId')

	def set_DatasourceId(self, DatasourceId):  # String
		self.add_path_param('DatasourceId', DatasourceId)
	def get_TableName(self): # String
		return self.get_path_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_path_param('TableName', TableName)
