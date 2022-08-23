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
from aliyunsdkmse.endpoint import endpoint_data
import json

class UpdateGatewayRouteRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdateGatewayRoute','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_GatewayUniqueId(self): # String
		return self.get_query_params().get('GatewayUniqueId')

	def set_GatewayUniqueId(self, GatewayUniqueId):  # String
		self.add_query_param('GatewayUniqueId', GatewayUniqueId)
	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_DomainIdListJSON(self): # String
		return self.get_query_params().get('DomainIdListJSON')

	def set_DomainIdListJSON(self, DomainIdListJSON):  # String
		self.add_query_param('DomainIdListJSON', DomainIdListJSON)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_GatewayId(self): # Long
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # Long
		self.add_query_param('GatewayId', GatewayId)
	def get_RouteOrder(self): # Integer
		return self.get_query_params().get('RouteOrder')

	def set_RouteOrder(self, RouteOrder):  # Integer
		self.add_query_param('RouteOrder', RouteOrder)
	def get_EnableWaf(self): # Boolean
		return self.get_query_params().get('EnableWaf')

	def set_EnableWaf(self, EnableWaf):  # Boolean
		self.add_query_param('EnableWaf', EnableWaf)
	def get_Services(self): # Array
		return self.get_query_params().get('Services')

	def set_Services(self, Services):  # Array
		self.add_query_param("Services", json.dumps(Services))
	def get_Predicates(self): # Struct
		return self.get_query_params().get('Predicates')

	def set_Predicates(self, Predicates):  # Struct
		self.add_query_param("Predicates", json.dumps(Predicates))
	def get_RedirectJSON(self): # Struct
		return self.get_query_params().get('RedirectJSON')

	def set_RedirectJSON(self, RedirectJSON):  # Struct
		self.add_query_param("RedirectJSON", json.dumps(RedirectJSON))
	def get_DirectResponseJSON(self): # Struct
		return self.get_query_params().get('DirectResponseJSON')

	def set_DirectResponseJSON(self, DirectResponseJSON):  # Struct
		self.add_query_param("DirectResponseJSON", json.dumps(DirectResponseJSON))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_FallbackServices(self): # Array
		return self.get_query_params().get('FallbackServices')

	def set_FallbackServices(self, FallbackServices):  # Array
		self.add_query_param("FallbackServices", json.dumps(FallbackServices))
	def get_Fallback(self): # Boolean
		return self.get_query_params().get('Fallback')

	def set_Fallback(self, Fallback):  # Boolean
		self.add_query_param('Fallback', Fallback)
