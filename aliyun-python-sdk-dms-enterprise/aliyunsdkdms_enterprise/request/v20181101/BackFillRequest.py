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
import json

class BackFillRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'BackFill','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DagId(self): # Long
		return self.get_query_params().get('DagId')

	def set_DagId(self, DagId):  # Long
		self.add_query_param('DagId', DagId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_IsTriggerSubTree(self): # Boolean
		return self.get_query_params().get('IsTriggerSubTree')

	def set_IsTriggerSubTree(self, IsTriggerSubTree):  # Boolean
		self.add_query_param('IsTriggerSubTree', IsTriggerSubTree)
	def get_BackFillDateEnd(self): # String
		return self.get_query_params().get('BackFillDateEnd')

	def set_BackFillDateEnd(self, BackFillDateEnd):  # String
		self.add_query_param('BackFillDateEnd', BackFillDateEnd)
	def get_HistoryDagId(self): # Long
		return self.get_query_params().get('HistoryDagId')

	def set_HistoryDagId(self, HistoryDagId):  # Long
		self.add_query_param('HistoryDagId', HistoryDagId)
	def get_StartNodeIds(self): # Array
		return self.get_query_params().get('StartNodeIds')

	def set_StartNodeIds(self, StartNodeIds):  # Array
		self.add_query_param("StartNodeIds", json.dumps(StartNodeIds))
	def get_FilterNodeIds(self): # Array
		return self.get_query_params().get('FilterNodeIds')

	def set_FilterNodeIds(self, FilterNodeIds):  # Array
		self.add_query_param("FilterNodeIds", json.dumps(FilterNodeIds))
	def get_BackFillDateBegin(self): # String
		return self.get_query_params().get('BackFillDateBegin')

	def set_BackFillDateBegin(self, BackFillDateBegin):  # String
		self.add_query_param('BackFillDateBegin', BackFillDateBegin)
	def get_BackFillDate(self): # String
		return self.get_query_params().get('BackFillDate')

	def set_BackFillDate(self, BackFillDate):  # String
		self.add_query_param('BackFillDate', BackFillDate)
	def get_Asc(self): # Boolean
		return self.get_query_params().get('Asc')

	def set_Asc(self, Asc):  # Boolean
		self.add_query_param('Asc', Asc)
	def get_Interval(self): # Integer
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Integer
		self.add_query_param('Interval', Interval)
