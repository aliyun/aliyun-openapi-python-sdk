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

class ListSlotsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'PAIElasticDatasetAccelerator', '2022-08-01', 'ListSlots','datasetacc')
		self.set_uri_pattern('/api/v1/slots')
		self.set_method('GET')

	def get_Phase(self): # String
		return self.get_query_params().get('Phase')

	def set_Phase(self, Phase):  # String
		self.add_query_param('Phase', Phase)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_EndpointIds(self): # String
		return self.get_query_params().get('EndpointIds')

	def set_EndpointIds(self, EndpointIds):  # String
		self.add_query_param('EndpointIds', EndpointIds)
	def get_SlotIds(self): # String
		return self.get_query_params().get('SlotIds')

	def set_SlotIds(self, SlotIds):  # String
		self.add_query_param('SlotIds', SlotIds)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SortBy(self): # String
		return self.get_query_params().get('SortBy')

	def set_SortBy(self, SortBy):  # String
		self.add_query_param('SortBy', SortBy)
	def get_StorageUri(self): # String
		return self.get_query_params().get('StorageUri')

	def set_StorageUri(self, StorageUri):  # String
		self.add_query_param('StorageUri', StorageUri)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
