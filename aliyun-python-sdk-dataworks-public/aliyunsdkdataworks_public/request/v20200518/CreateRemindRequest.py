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

class CreateRemindRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateRemind')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DndEnd(self):
		return self.get_body_params().get('DndEnd')

	def set_DndEnd(self,DndEnd):
		self.add_body_params('DndEnd', DndEnd)

	def get_AlertUnit(self):
		return self.get_body_params().get('AlertUnit')

	def set_AlertUnit(self,AlertUnit):
		self.add_body_params('AlertUnit', AlertUnit)

	def get_RemindUnit(self):
		return self.get_body_params().get('RemindUnit')

	def set_RemindUnit(self,RemindUnit):
		self.add_body_params('RemindUnit', RemindUnit)

	def get_AlertInterval(self):
		return self.get_body_params().get('AlertInterval')

	def set_AlertInterval(self,AlertInterval):
		self.add_body_params('AlertInterval', AlertInterval)

	def get_AlertMethods(self):
		return self.get_body_params().get('AlertMethods')

	def set_AlertMethods(self,AlertMethods):
		self.add_body_params('AlertMethods', AlertMethods)

	def get_RobotUrls(self):
		return self.get_body_params().get('RobotUrls')

	def set_RobotUrls(self,RobotUrls):
		self.add_body_params('RobotUrls', RobotUrls)

	def get_MaxAlertTimes(self):
		return self.get_body_params().get('MaxAlertTimes')

	def set_MaxAlertTimes(self,MaxAlertTimes):
		self.add_body_params('MaxAlertTimes', MaxAlertTimes)

	def get_BizProcessIds(self):
		return self.get_body_params().get('BizProcessIds')

	def set_BizProcessIds(self,BizProcessIds):
		self.add_body_params('BizProcessIds', BizProcessIds)

	def get_RemindType(self):
		return self.get_body_params().get('RemindType')

	def set_RemindType(self,RemindType):
		self.add_body_params('RemindType', RemindType)

	def get_AlertTargets(self):
		return self.get_body_params().get('AlertTargets')

	def set_AlertTargets(self,AlertTargets):
		self.add_body_params('AlertTargets', AlertTargets)

	def get_BaselineIds(self):
		return self.get_body_params().get('BaselineIds')

	def set_BaselineIds(self,BaselineIds):
		self.add_body_params('BaselineIds', BaselineIds)

	def get_Detail(self):
		return self.get_body_params().get('Detail')

	def set_Detail(self,Detail):
		self.add_body_params('Detail', Detail)

	def get_RemindName(self):
		return self.get_body_params().get('RemindName')

	def set_RemindName(self,RemindName):
		self.add_body_params('RemindName', RemindName)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_NodeIds(self):
		return self.get_body_params().get('NodeIds')

	def set_NodeIds(self,NodeIds):
		self.add_body_params('NodeIds', NodeIds)