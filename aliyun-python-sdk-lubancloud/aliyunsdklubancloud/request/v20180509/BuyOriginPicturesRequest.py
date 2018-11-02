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
class BuyOriginPicturesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lubancloud', '2018-05-09', 'BuyOriginPictures','luban')
		self.set_method('POST')

	def get_PictureIds(self):
		return self.get_query_params().get('PictureIds')

	def set_PictureIds(self,PictureIds):
		for i in range(len(PictureIds)):	
			if PictureIds[i] is not None:
				self.add_query_param('PictureId.' + str(i + 1) , PictureIds[i]);