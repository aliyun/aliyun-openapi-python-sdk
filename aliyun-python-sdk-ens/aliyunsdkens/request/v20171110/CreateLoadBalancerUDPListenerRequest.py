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

class CreateLoadBalancerUDPListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateLoadBalancerUDPListener','ens')
		self.set_method('POST')

	def get_EstablishedTimeout(self): # Integer
		return self.get_query_params().get('EstablishedTimeout')

	def set_EstablishedTimeout(self, EstablishedTimeout):  # Integer
		self.add_query_param('EstablishedTimeout', EstablishedTimeout)
	def get_LoadBalancerId(self): # String
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_query_param('LoadBalancerId', LoadBalancerId)
	def get_HealthCheckReq(self): # String
		return self.get_query_params().get('HealthCheckReq')

	def set_HealthCheckReq(self, HealthCheckReq):  # String
		self.add_query_param('HealthCheckReq', HealthCheckReq)
	def get_HealthCheckInterval(self): # Integer
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self, HealthCheckInterval):  # Integer
		self.add_query_param('HealthCheckInterval', HealthCheckInterval)
	def get_BackendServerPort(self): # Integer
		return self.get_query_params().get('BackendServerPort')

	def set_BackendServerPort(self, BackendServerPort):  # Integer
		self.add_query_param('BackendServerPort', BackendServerPort)
	def get_HealthCheckExp(self): # String
		return self.get_query_params().get('HealthCheckExp')

	def set_HealthCheckExp(self, HealthCheckExp):  # String
		self.add_query_param('HealthCheckExp', HealthCheckExp)
	def get_HealthCheckConnectTimeout(self): # Integer
		return self.get_query_params().get('HealthCheckConnectTimeout')

	def set_HealthCheckConnectTimeout(self, HealthCheckConnectTimeout):  # Integer
		self.add_query_param('HealthCheckConnectTimeout', HealthCheckConnectTimeout)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_UnhealthyThreshold(self): # Integer
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self, UnhealthyThreshold):  # Integer
		self.add_query_param('UnhealthyThreshold', UnhealthyThreshold)
	def get_HealthyThreshold(self): # Integer
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self, HealthyThreshold):  # Integer
		self.add_query_param('HealthyThreshold', HealthyThreshold)
	def get_Scheduler(self): # String
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_query_param('Scheduler', Scheduler)
	def get_EipTransmit(self): # String
		return self.get_query_params().get('EipTransmit')

	def set_EipTransmit(self, EipTransmit):  # String
		self.add_query_param('EipTransmit', EipTransmit)
	def get_ListenerPort(self): # Integer
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_query_param('ListenerPort', ListenerPort)
	def get_HealthCheckConnectPort(self): # Integer
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self, HealthCheckConnectPort):  # Integer
		self.add_query_param('HealthCheckConnectPort', HealthCheckConnectPort)
