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
from aliyunsdkccc.endpoint import endpoint_data

class AddPhoneTagsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'AddPhoneTags')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RegionNameProvince(self):
		return self.get_query_params().get('RegionNameProvince')

	def set_RegionNameProvince(self,RegionNameProvince):
		self.add_query_param('RegionNameProvince',RegionNameProvince)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Concurrency(self):
		return self.get_query_params().get('Concurrency')

	def set_Concurrency(self,Concurrency):
		self.add_query_param('Concurrency',Concurrency)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Provider(self):
		return self.get_query_params().get('Provider')

	def set_Provider(self,Provider):
		self.add_query_param('Provider',Provider)

	def get_PhoneNumberLists(self):
		return self.get_query_params().get('PhoneNumberLists')

	def set_PhoneNumberLists(self,PhoneNumberLists):
		for i in range(len(PhoneNumberLists)):	
			if PhoneNumberLists[i] is not None:
				self.add_query_param('PhoneNumberList.' + str(i + 1) , PhoneNumberLists[i]);

	def get_ServiceTag(self):
		return self.get_query_params().get('ServiceTag')

	def set_ServiceTag(self,ServiceTag):
		self.add_query_param('ServiceTag',ServiceTag)

	def get_RegionNameCity(self):
		return self.get_query_params().get('RegionNameCity')

	def set_RegionNameCity(self,RegionNameCity):
		self.add_query_param('RegionNameCity',RegionNameCity)