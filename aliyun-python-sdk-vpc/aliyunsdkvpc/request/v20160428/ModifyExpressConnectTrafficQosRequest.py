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
from aliyunsdkvpc.endpoint import endpoint_data

class ModifyExpressConnectTrafficQosRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyExpressConnectTrafficQos','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RemoveInstanceLists(self): # RepeatList
		return self.get_query_params().get('RemoveInstanceList')

	def set_RemoveInstanceLists(self, RemoveInstanceList):  # RepeatList
		for depth1 in range(len(RemoveInstanceList)):
			if RemoveInstanceList[depth1].get('InstanceId') is not None:
				self.add_query_param('RemoveInstanceList.' + str(depth1 + 1) + '.InstanceId', RemoveInstanceList[depth1].get('InstanceId'))
			if RemoveInstanceList[depth1].get('InstanceType') is not None:
				self.add_query_param('RemoveInstanceList.' + str(depth1 + 1) + '.InstanceType', RemoveInstanceList[depth1].get('InstanceType'))
	def get_AddInstanceLists(self): # RepeatList
		return self.get_query_params().get('AddInstanceList')

	def set_AddInstanceLists(self, AddInstanceList):  # RepeatList
		for depth1 in range(len(AddInstanceList)):
			if AddInstanceList[depth1].get('InstanceId') is not None:
				self.add_query_param('AddInstanceList.' + str(depth1 + 1) + '.InstanceId', AddInstanceList[depth1].get('InstanceId'))
			if AddInstanceList[depth1].get('InstanceType') is not None:
				self.add_query_param('AddInstanceList.' + str(depth1 + 1) + '.InstanceType', AddInstanceList[depth1].get('InstanceType'))
	def get_QosId(self): # String
		return self.get_query_params().get('QosId')

	def set_QosId(self, QosId):  # String
		self.add_query_param('QosId', QosId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_QosName(self): # String
		return self.get_query_params().get('QosName')

	def set_QosName(self, QosName):  # String
		self.add_query_param('QosName', QosName)
	def get_QosDescription(self): # String
		return self.get_query_params().get('QosDescription')

	def set_QosDescription(self, QosDescription):  # String
		self.add_query_param('QosDescription', QosDescription)
