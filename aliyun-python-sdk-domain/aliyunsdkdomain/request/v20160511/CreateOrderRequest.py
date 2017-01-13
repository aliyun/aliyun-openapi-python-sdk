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
		return self._subOrderParams

	def set_SubOrderParams(self, SubOrderParams):
		self._subOrderParams = SubOrderParams;
		for i in range(len(SubOrderParams)):
			self.add_query_param("SubOrderParam.%d.SaleID" %(i+1), SubOrderParams[i].get_SaleID());
			self.add_query_param("SubOrderParam.%d.RelatedName" % (i+1), SubOrderParams[i].get_RelatedName());
			self.add_query_param("SubOrderParam.%d.Action" % (i+1) , SubOrderParams[i].get_Action());
			self.add_query_param("SubOrderParam.%d.Period" % (i+1), SubOrderParams[i].get_Period());
			self.add_query_param("SubOrderParam.%d.DomainTemplateID" % (i+1), SubOrderParams[i].get_DomainTemplateID());

class SubOrderParam(object):
	def __init__(self):
		self._SaleID = ''
		self._RelatedName = ''
		self._Action = ''
		self._Period = 0
		self._DomainTemplateID = ''

	def get_SaleID(self):
		return self._SaleID

	def set_SaleID(self, SaleID):
		self._SaleID = SaleID

	def get_RelatedName(self):
		return self._RelatedName

	def set_RelatedName(self, RelatedName):
		self._RelatedName = RelatedName

	def get_Action(self):
		return self._Action

	def set_Action(self, Action):
		self._Action = Action

	def get_Period(self):
		return self._Period

	def set_Period(self, Period):
		self._Period = Period

	def get_DomainTemplateID(self):
		return self._DomainTemplateID

	def set_DomainTemplateID(self, DomainTemplateID):
		self._DomainTemplateID = DomainTemplateID