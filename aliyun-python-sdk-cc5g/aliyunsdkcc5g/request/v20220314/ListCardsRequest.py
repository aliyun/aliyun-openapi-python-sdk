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

class ListCardsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'ListCards','fivegcc')
		self.set_method('GET')

	def get_IpAddress(self): # String
		return self.get_query_params().get('IpAddress')

	def set_IpAddress(self, IpAddress):  # String
		self.add_query_param('IpAddress', IpAddress)
	def get_Iccids(self): # Array
		return self.get_query_params().get('Iccids')

	def set_Iccids(self, Iccids):  # Array
		for index1, value1 in enumerate(Iccids):
			self.add_query_param('Iccids.' + str(index1 + 1), value1)
	def get_Iccid(self): # String
		return self.get_query_params().get('Iccid')

	def set_Iccid(self, Iccid):  # String
		self.add_query_param('Iccid', Iccid)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Lock(self): # Boolean
		return self.get_query_params().get('Lock')

	def set_Lock(self, Lock):  # Boolean
		self.add_query_param('Lock', Lock)
	def get_Msisdn(self): # String
		return self.get_query_params().get('Msisdn')

	def set_Msisdn(self, Msisdn):  # String
		self.add_query_param('Msisdn', Msisdn)
	def get_Apn(self): # String
		return self.get_query_params().get('Apn')

	def set_Apn(self, Apn):  # String
		self.add_query_param('Apn', Apn)
	def get_NetLinkId(self): # String
		return self.get_query_params().get('NetLinkId')

	def set_NetLinkId(self, NetLinkId):  # String
		self.add_query_param('NetLinkId', NetLinkId)
	def get_WirelessCloudConnectorId(self): # String
		return self.get_query_params().get('WirelessCloudConnectorId')

	def set_WirelessCloudConnectorId(self, WirelessCloudConnectorId):  # String
		self.add_query_param('WirelessCloudConnectorId', WirelessCloudConnectorId)
	def get_Online(self): # Boolean
		return self.get_query_params().get('Online')

	def set_Online(self, Online):  # Boolean
		self.add_query_param('Online', Online)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_Statuses(self): # Array
		return self.get_query_params().get('Statuses')

	def set_Statuses(self, Statuses):  # Array
		for index1, value1 in enumerate(Statuses):
			self.add_query_param('Statuses.' + str(index1 + 1), value1)
