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

class CreateHoneypotProbeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateHoneypotProbe','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ControlNodeId(self): # String
		return self.get_query_params().get('ControlNodeId')

	def set_ControlNodeId(self, ControlNodeId):  # String
		self.add_query_param('ControlNodeId', ControlNodeId)
	def get_ProxyIp(self): # String
		return self.get_query_params().get('ProxyIp')

	def set_ProxyIp(self, ProxyIp):  # String
		self.add_query_param('ProxyIp', ProxyIp)
	def get_Ping(self): # Boolean
		return self.get_query_params().get('Ping')

	def set_Ping(self, Ping):  # Boolean
		self.add_query_param('Ping', Ping)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_ProbeVersion(self): # String
		return self.get_query_params().get('ProbeVersion')

	def set_ProbeVersion(self, ProbeVersion):  # String
		self.add_query_param('ProbeVersion', ProbeVersion)
	def get_HoneypotBindLists(self): # RepeatList
		return self.get_query_params().get('HoneypotBindList')

	def set_HoneypotBindLists(self, HoneypotBindList):  # RepeatList
		for depth1 in range(len(HoneypotBindList)):
			if HoneypotBindList[depth1].get('BindPortList') is not None:
				for depth2 in range(len(HoneypotBindList[depth1].get('BindPortList'))):
					if HoneypotBindList[depth1].get('BindPortList')[depth2].get('StartPort') is not None:
						self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.BindPortList.'  + str(depth2 + 1) + '.StartPort', HoneypotBindList[depth1].get('BindPortList')[depth2].get('StartPort'))
					if HoneypotBindList[depth1].get('BindPortList')[depth2].get('BindPort') is not None:
						self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.BindPortList.'  + str(depth2 + 1) + '.BindPort', HoneypotBindList[depth1].get('BindPortList')[depth2].get('BindPort'))
					if HoneypotBindList[depth1].get('BindPortList')[depth2].get('Fixed') is not None:
						self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.BindPortList.'  + str(depth2 + 1) + '.Fixed', HoneypotBindList[depth1].get('BindPortList')[depth2].get('Fixed'))
					if HoneypotBindList[depth1].get('BindPortList')[depth2].get('EndPort') is not None:
						self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.BindPortList.'  + str(depth2 + 1) + '.EndPort', HoneypotBindList[depth1].get('BindPortList')[depth2].get('EndPort'))
					if HoneypotBindList[depth1].get('BindPortList')[depth2].get('TargetPort') is not None:
						self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.BindPortList.'  + str(depth2 + 1) + '.TargetPort', HoneypotBindList[depth1].get('BindPortList')[depth2].get('TargetPort'))
			if HoneypotBindList[depth1].get('HoneypotId') is not None:
				self.add_query_param('HoneypotBindList.' + str(depth1 + 1) + '.HoneypotId', HoneypotBindList[depth1].get('HoneypotId'))
	def get_Arp(self): # Boolean
		return self.get_query_params().get('Arp')

	def set_Arp(self, Arp):  # Boolean
		self.add_query_param('Arp', Arp)
	def get_ProbeType(self): # String
		return self.get_query_params().get('ProbeType')

	def set_ProbeType(self, ProbeType):  # String
		self.add_query_param('ProbeType', ProbeType)
	def get_BusinessGroupId(self): # String
		return self.get_query_params().get('BusinessGroupId')

	def set_BusinessGroupId(self, BusinessGroupId):  # String
		self.add_query_param('BusinessGroupId', BusinessGroupId)
	def get_DisplayName(self): # String
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_query_param('DisplayName', DisplayName)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
