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
from aliyunsdkimm.endpoint import endpoint_data
import json

class QueryStoriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'QueryStories','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FigureClusterIds(self): # Array
		return self.get_query_params().get('FigureClusterIds')

	def set_FigureClusterIds(self, FigureClusterIds):  # Array
		self.add_query_param("FigureClusterIds", json.dumps(FigureClusterIds))
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_CustomLabels(self): # String
		return self.get_query_params().get('CustomLabels')

	def set_CustomLabels(self, CustomLabels):  # String
		self.add_query_param('CustomLabels', CustomLabels)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_StoryType(self): # String
		return self.get_query_params().get('StoryType')

	def set_StoryType(self, StoryType):  # String
		self.add_query_param('StoryType', StoryType)
	def get_StoryEndTimeRange(self): # Struct
		return self.get_query_params().get('StoryEndTimeRange')

	def set_StoryEndTimeRange(self, StoryEndTimeRange):  # Struct
		self.add_query_param("StoryEndTimeRange", json.dumps(StoryEndTimeRange))
	def get_WithEmptyStories(self): # Boolean
		return self.get_query_params().get('WithEmptyStories')

	def set_WithEmptyStories(self, WithEmptyStories):  # Boolean
		self.add_query_param('WithEmptyStories', WithEmptyStories)
	def get_StoryStartTimeRange(self): # Struct
		return self.get_query_params().get('StoryStartTimeRange')

	def set_StoryStartTimeRange(self, StoryStartTimeRange):  # Struct
		self.add_query_param("StoryStartTimeRange", json.dumps(StoryStartTimeRange))
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_StorySubType(self): # String
		return self.get_query_params().get('StorySubType')

	def set_StorySubType(self, StorySubType):  # String
		self.add_query_param('StorySubType', StorySubType)
	def get_CreateTimeRange(self): # Struct
		return self.get_query_params().get('CreateTimeRange')

	def set_CreateTimeRange(self, CreateTimeRange):  # Struct
		self.add_query_param("CreateTimeRange", json.dumps(CreateTimeRange))
	def get_DatasetName(self): # String
		return self.get_query_params().get('DatasetName')

	def set_DatasetName(self, DatasetName):  # String
		self.add_query_param('DatasetName', DatasetName)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_ObjectId(self): # String
		return self.get_query_params().get('ObjectId')

	def set_ObjectId(self, ObjectId):  # String
		self.add_query_param('ObjectId', ObjectId)
	def get_StoryName(self): # String
		return self.get_query_params().get('StoryName')

	def set_StoryName(self, StoryName):  # String
		self.add_query_param('StoryName', StoryName)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
