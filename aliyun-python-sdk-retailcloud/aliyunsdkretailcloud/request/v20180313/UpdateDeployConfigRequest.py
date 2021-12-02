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
from aliyunsdkretailcloud.endpoint import endpoint_data

class UpdateDeployConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'UpdateDeployConfig')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CodePath(self): # String
		return self.get_query_params().get('CodePath')

	def set_CodePath(self, CodePath):  # String
		self.add_query_param('CodePath', CodePath)
	def get_ConfigMapLists(self): # RepeatList
		return self.get_query_params().get('ConfigMapList')

	def set_ConfigMapLists(self, ConfigMapList):  # RepeatList
		for depth1 in range(len(ConfigMapList)):
			self.add_query_param('ConfigMapList.' + str(depth1 + 1), ConfigMapList[depth1])
	def get_ConfigMap(self): # String
		return self.get_query_params().get('ConfigMap')

	def set_ConfigMap(self, ConfigMap):  # String
		self.add_query_param('ConfigMap', ConfigMap)
	def get_StatefulSet(self): # String
		return self.get_query_params().get('StatefulSet')

	def set_StatefulSet(self, StatefulSet):  # String
		self.add_query_param('StatefulSet', StatefulSet)
	def get_AppId(self): # Long
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # Long
		self.add_query_param('AppId', AppId)
	def get_SecretLists(self): # RepeatList
		return self.get_query_params().get('SecretList')

	def set_SecretLists(self, SecretList):  # RepeatList
		for depth1 in range(len(SecretList)):
			self.add_query_param('SecretList.' + str(depth1 + 1), SecretList[depth1])
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_CronJob(self): # String
		return self.get_query_params().get('CronJob')

	def set_CronJob(self, CronJob):  # String
		self.add_query_param('CronJob', CronJob)
	def get_Deployment(self): # String
		return self.get_query_params().get('Deployment')

	def set_Deployment(self, Deployment):  # String
		self.add_query_param('Deployment', Deployment)
