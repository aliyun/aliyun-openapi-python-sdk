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
class OnsTopicCreateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ons', '2017-09-18', 'OnsTopicCreate')

	def get_PreventCache(self):
		return self.get_query_params().get('PreventCache')

	def set_PreventCache(self,PreventCache):
		self.add_query_param('PreventCache',PreventCache)

	def get_Cluster(self):
		return self.get_query_params().get('Cluster')

	def set_Cluster(self,Cluster):
		self.add_query_param('Cluster',Cluster)

	def get_QueueNum(self):
		return self.get_query_params().get('QueueNum')

	def set_QueueNum(self,QueueNum):
		self.add_query_param('QueueNum',QueueNum)

	def get_OnsRegionId(self):
		return self.get_query_params().get('OnsRegionId')

	def set_OnsRegionId(self,OnsRegionId):
		self.add_query_param('OnsRegionId',OnsRegionId)

	def get_OnsPlatform(self):
		return self.get_query_params().get('OnsPlatform')

	def set_OnsPlatform(self,OnsPlatform):
		self.add_query_param('OnsPlatform',OnsPlatform)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_Qps(self):
		return self.get_query_params().get('Qps')

	def set_Qps(self,Qps):
		self.add_query_param('Qps',Qps)

	def get_Topic(self):
		return self.get_query_params().get('Topic')

	def set_Topic(self,Topic):
		self.add_query_param('Topic',Topic)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Appkey(self):
		return self.get_query_params().get('Appkey')

	def set_Appkey(self,Appkey):
		self.add_query_param('Appkey',Appkey)

	def get_Order(self):
		return self.get_query_params().get('Order')

	def set_Order(self,Order):
		self.add_query_param('Order',Order)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)