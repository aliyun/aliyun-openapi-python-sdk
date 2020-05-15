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
from aliyunsdkiot.endpoint import endpoint_data

class BatchAddThingTopoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'BatchAddThingTopo','Iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GwProductKey(self):
		return self.get_query_params().get('GwProductKey')

	def set_GwProductKey(self,GwProductKey):
		self.add_query_param('GwProductKey',GwProductKey)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_TopoAddItems(self):
		return self.get_query_params().get('TopoAddItems')

	def set_TopoAddItems(self, TopoAddItems):
		for depth1 in range(len(TopoAddItems)):
			if TopoAddItems[depth1].get('ClientId') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.ClientId', TopoAddItems[depth1].get('ClientId'))
			if TopoAddItems[depth1].get('SignMethod') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.SignMethod', TopoAddItems[depth1].get('SignMethod'))
			if TopoAddItems[depth1].get('Sign') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.Sign', TopoAddItems[depth1].get('Sign'))
			if TopoAddItems[depth1].get('DeviceName') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.DeviceName', TopoAddItems[depth1].get('DeviceName'))
			if TopoAddItems[depth1].get('ProductKey') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.ProductKey', TopoAddItems[depth1].get('ProductKey'))
			if TopoAddItems[depth1].get('Timestamp') is not None:
				self.add_query_param('TopoAddItem.' + str(depth1 + 1) + '.Timestamp', TopoAddItems[depth1].get('Timestamp'))

	def get_GwDeviceName(self):
		return self.get_query_params().get('GwDeviceName')

	def set_GwDeviceName(self,GwDeviceName):
		self.add_query_param('GwDeviceName',GwDeviceName)