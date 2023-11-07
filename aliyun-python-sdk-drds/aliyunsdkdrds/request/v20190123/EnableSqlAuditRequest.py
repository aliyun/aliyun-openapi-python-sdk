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
from aliyunsdkdrds.endpoint import endpoint_data

class EnableSqlAuditRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'EnableSqlAudit','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RecallStartTimestamp(self): # String
		return self.get_query_params().get('RecallStartTimestamp')

	def set_RecallStartTimestamp(self, RecallStartTimestamp):  # String
		self.add_query_param('RecallStartTimestamp', RecallStartTimestamp)
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
	def get_IsRecall(self): # Boolean
		return self.get_query_params().get('IsRecall')

	def set_IsRecall(self, IsRecall):  # Boolean
		self.add_query_param('IsRecall', IsRecall)
	def get_RecallEndTimestamp(self): # String
		return self.get_query_params().get('RecallEndTimestamp')

	def set_RecallEndTimestamp(self, RecallEndTimestamp):  # String
		self.add_query_param('RecallEndTimestamp', RecallEndTimestamp)
