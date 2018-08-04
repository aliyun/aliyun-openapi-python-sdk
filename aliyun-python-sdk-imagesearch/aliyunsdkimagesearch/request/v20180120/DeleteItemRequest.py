# -- coding: utf-8 --

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
import base64
from aliyunsdkcore.request import RoaRequest
class DeleteItemRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ImageSearch', '2018-01-20', 'DeleteItem','imagesearch')
		self.set_uri_pattern('/item/delete')
		self.set_method('POST')
		self.set_accept_format('JSON')
		self.item_id = None
		self.pic_list = []

	def get_instance_name(self):
		return self.get_query_params().get('instanceName')

	def set_instance_name(self,instanceName):
		self.add_query_param('instanceName',instanceName)

	def set_item_id(self, item_id):
		self.item_id = item_id
	
	def get_item_id(self):
		return self.item_id

	def add_picture(self, pic_name):
		self.pic_list.append(pic_name)

	# Build Post Content
	def build_post_content(self):
		param_map = {}
		# 参数判断
		if not self.item_id :
			return False
		# 构建参数
		param_map['item_id'] = self.item_id

		# 遍历图片列表
		pic_list_str = ''
		for pic_name in self.pic_list:
			if len(pic_list_str) > 0:
				pic_list_str += ','
			encode_pic_name = base64.b64encode(pic_name)
			pic_list_str += encode_pic_name
		
		param_map['pic_list'] = pic_list_str

		self.set_content(self.build_content(param_map))

		return True

	# 构建POST的Body内容
	def build_content(self, param_map):
		# 变量
		meta = ''
		body = ''
		start = 0

		# 遍历参数
		for key in param_map:
			if len(meta) > 0:
				meta += '#'
			meta += key + ',' + str(start) + ',' + str(start + len(param_map[key]))
			body += param_map[key]
			start += len(param_map[key])
		return meta + '^' + body