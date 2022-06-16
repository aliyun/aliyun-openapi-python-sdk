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
from aliyunsdkedas.endpoint import endpoint_data

class BindK8sSlbRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'BindK8sSlb','Edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_slb_binding')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Scheduler(self): # string
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # string
		self.add_query_param('Scheduler', Scheduler)
	def get_ServicePortInfos(self): # string
		return self.get_query_params().get('ServicePortInfos')

	def set_ServicePortInfos(self, ServicePortInfos):  # string
		self.add_query_param('ServicePortInfos', ServicePortInfos)
	def get_SlbId(self): # string
		return self.get_query_params().get('SlbId')

	def set_SlbId(self, SlbId):  # string
		self.add_query_param('SlbId', SlbId)
	def get_SlbProtocol(self): # string
		return self.get_query_params().get('SlbProtocol')

	def set_SlbProtocol(self, SlbProtocol):  # string
		self.add_query_param('SlbProtocol', SlbProtocol)
	def get_Port(self): # string
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # string
		self.add_query_param('Port', Port)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_Specification(self): # string
		return self.get_query_params().get('Specification')

	def set_Specification(self, Specification):  # string
		self.add_query_param('Specification', Specification)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
	def get_Type(self): # string
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # string
		self.add_query_param('Type', Type)
	def get_TargetPort(self): # string
		return self.get_query_params().get('TargetPort')

	def set_TargetPort(self, TargetPort):  # string
		self.add_query_param('TargetPort', TargetPort)
