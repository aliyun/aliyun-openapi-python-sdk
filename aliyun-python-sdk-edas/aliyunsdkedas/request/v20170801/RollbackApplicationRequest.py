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
from aliyunsdkedas.endpoint import endpoint_data

class RollbackApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'RollbackApplication','edas')
		self.set_uri_pattern('/pop/v5/changeorder/co_rollback')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_BatchWaitTime(self):
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self,BatchWaitTime):
		self.add_query_param('BatchWaitTime',BatchWaitTime)

	def get_Batch(self):
		return self.get_query_params().get('Batch')

	def set_Batch(self,Batch):
		self.add_query_param('Batch',Batch)

	def get_HistoryVersion(self):
		return self.get_query_params().get('HistoryVersion')

	def set_HistoryVersion(self,HistoryVersion):
		self.add_query_param('HistoryVersion',HistoryVersion)