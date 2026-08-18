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

class PushMeteringDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'marketplaceIntl', '2022-12-30', 'PushMeteringData')
		self.set_method('POST')

	def get_MeteringDatas(self): # RepeatList
		return self.get_body_params().get('MeteringData')

	def set_MeteringDatas(self, MeteringData):  # RepeatList
		for depth1 in range(len(MeteringData)):
			if MeteringData[depth1].get('MeteringAssist') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.MeteringAssist', MeteringData[depth1].get('MeteringAssist'))
			if MeteringData[depth1].get('PushOrderBizId') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.PushOrderBizId', MeteringData[depth1].get('PushOrderBizId'))
			if MeteringData[depth1].get('InstanceId') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.InstanceId', MeteringData[depth1].get('InstanceId'))
			if MeteringData[depth1].get('EndTime') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.EndTime', MeteringData[depth1].get('EndTime'))
			if MeteringData[depth1].get('StartTime') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.StartTime', MeteringData[depth1].get('StartTime'))
			if MeteringData[depth1].get('MeteringEntity') is not None:
				self.add_body_params('MeteringData.' + str(depth1 + 1) + '.MeteringEntity', MeteringData[depth1].get('MeteringEntity'))
	def get_GmtCreate(self): # String
		return self.get_body_params().get('GmtCreate')

	def set_GmtCreate(self, GmtCreate):  # String
		self.add_body_params('GmtCreate', GmtCreate)
