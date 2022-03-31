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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class ListTaskFlowInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'ListTaskFlowInstance','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TriggerType(self): # Integer
		return self.get_query_params().get('TriggerType')

	def set_TriggerType(self, TriggerType):  # Integer
		self.add_query_param('TriggerType', TriggerType)
	def get_DagId(self): # Long
		return self.get_query_params().get('DagId')

	def set_DagId(self, DagId):  # Long
		self.add_query_param('DagId', DagId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_PageIndex(self): # Integer
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self, PageIndex):  # Integer
		self.add_query_param('PageIndex', PageIndex)
	def get_StartTimeBegin(self): # String
		return self.get_query_params().get('StartTimeBegin')

	def set_StartTimeBegin(self, StartTimeBegin):  # String
		self.add_query_param('StartTimeBegin', StartTimeBegin)
	def get_StartTimeEnd(self): # String
		return self.get_query_params().get('StartTimeEnd')

	def set_StartTimeEnd(self, StartTimeEnd):  # String
		self.add_query_param('StartTimeEnd', StartTimeEnd)
