# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2016-05-11', 'CreateOrder')

	def get_SubOrderParams(self):
		return self.get_query_params().get('SubOrderParams')

	def set_SubOrderParams(self,SubOrderParams):
		for i in range(len(SubOrderParams)):	
			self.add_query_param('SubOrderParam.' + bytes(i + 1) + '.SaleID' , SubOrderParams[i].get('SaleID'))
			self.add_query_param('SubOrderParam.' + bytes(i + 1) + '.RelatedName' , SubOrderParams[i].get('RelatedName'))
			self.add_query_param('SubOrderParam.' + bytes(i + 1) + '.Action' , SubOrderParams[i].get('Action'))
			self.add_query_param('SubOrderParam.' + bytes(i + 1) + '.Period' , SubOrderParams[i].get('Period'))
			self.add_query_param('SubOrderParam.' + bytes(i + 1) + '.DomainTemplateID' , SubOrderParams[i].get('DomainTemplateID'))
