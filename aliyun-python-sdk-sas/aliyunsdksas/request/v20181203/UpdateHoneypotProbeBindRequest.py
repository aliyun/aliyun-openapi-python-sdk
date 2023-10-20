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
from aliyunsdksas.endpoint import endpoint_data

class UpdateHoneypotProbeBindRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'UpdateHoneypotProbeBind','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProbeId(self): # String
		return self.get_query_params().get('ProbeId')

	def set_ProbeId(self, ProbeId):  # String
		self.add_query_param('ProbeId', ProbeId)
	def get_Ports(self): # String
		return self.get_query_params().get('Ports')

	def set_Ports(self, Ports):  # String
		self.add_query_param('Ports', Ports)
	def get_BindPortLists(self): # RepeatList
		return self.get_query_params().get('BindPortList')

	def set_BindPortLists(self, BindPortList):  # RepeatList
		for depth1 in range(len(BindPortList)):
			if BindPortList[depth1].get('StartPort') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.StartPort', BindPortList[depth1].get('StartPort'))
			if BindPortList[depth1].get('BindPort') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.BindPort', BindPortList[depth1].get('BindPort'))
			if BindPortList[depth1].get('Proto') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.Proto', BindPortList[depth1].get('Proto'))
			if BindPortList[depth1].get('Fixed') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.Fixed', BindPortList[depth1].get('Fixed'))
			if BindPortList[depth1].get('Id') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.Id', BindPortList[depth1].get('Id'))
			if BindPortList[depth1].get('EndPort') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.EndPort', BindPortList[depth1].get('EndPort'))
			if BindPortList[depth1].get('TargetPort') is not None:
				self.add_query_param('BindPortList.' + str(depth1 + 1) + '.TargetPort', BindPortList[depth1].get('TargetPort'))
	def get_ServiceIpLists(self): # RepeatList
		return self.get_query_params().get('ServiceIpList')

	def set_ServiceIpLists(self, ServiceIpList):  # RepeatList
		for depth1 in range(len(ServiceIpList)):
			self.add_query_param('ServiceIpList.' + str(depth1 + 1), ServiceIpList[depth1])
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_SetStatus(self): # Integer
		return self.get_query_params().get('SetStatus')

	def set_SetStatus(self, SetStatus):  # Integer
		self.add_query_param('SetStatus', SetStatus)
	def get_HoneypotId(self): # String
		return self.get_query_params().get('HoneypotId')

	def set_HoneypotId(self, HoneypotId):  # String
		self.add_query_param('HoneypotId', HoneypotId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_BindId(self): # String
		return self.get_query_params().get('BindId')

	def set_BindId(self, BindId):  # String
		self.add_query_param('BindId', BindId)
	def get_BindType(self): # String
		return self.get_query_params().get('BindType')

	def set_BindType(self, BindType):  # String
		self.add_query_param('BindType', BindType)
