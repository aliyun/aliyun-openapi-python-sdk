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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class DsgQuerySensResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'DsgQuerySensResult')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Col(self): # String
		return self.get_body_params().get('Col')

	def set_Col(self, Col):  # String
		self.add_body_params('Col', Col)
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_SchemaName(self): # String
		return self.get_body_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_body_params('SchemaName', SchemaName)
	def get_Level(self): # String
		return self.get_body_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_body_params('Level', Level)
	def get_SensStatus(self): # String
		return self.get_body_params().get('SensStatus')

	def set_SensStatus(self, SensStatus):  # String
		self.add_body_params('SensStatus', SensStatus)
	def get_NodeName(self): # String
		return self.get_body_params().get('NodeName')

	def set_NodeName(self, NodeName):  # String
		self.add_body_params('NodeName', NodeName)
	def get_SensitiveId(self): # String
		return self.get_body_params().get('SensitiveId')

	def set_SensitiveId(self, SensitiveId):  # String
		self.add_body_params('SensitiveId', SensitiveId)
	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_DbType(self): # String
		return self.get_body_params().get('DbType')

	def set_DbType(self, DbType):  # String
		self.add_body_params('DbType', DbType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_SensitiveName(self): # String
		return self.get_body_params().get('SensitiveName')

	def set_SensitiveName(self, SensitiveName):  # String
		self.add_body_params('SensitiveName', SensitiveName)
	def get_Table(self): # String
		return self.get_body_params().get('Table')

	def set_Table(self, Table):  # String
		self.add_body_params('Table', Table)
	def get_Order(self): # String
		return self.get_body_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_body_params('Order', Order)
	def get_OrderField(self): # String
		return self.get_body_params().get('OrderField')

	def set_OrderField(self, OrderField):  # String
		self.add_body_params('OrderField', OrderField)
