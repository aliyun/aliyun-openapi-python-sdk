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
class AddItemRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ImageSearch', '2018-01-20', 'AddItem','imagesearch')
		self.set_uri_pattern('/item/add')
		self.set_method('POST')
		self.set_accept_format('JSON')
		self.item_id = ''
		self.cate_id = ''
		self.cust_content = ''
		self.pic_map = {}

	def get_instance_name(self):
		return self.get_query_params().get('instanceName')

	def set_instance_name(self,instanceName):
		self.add_query_param('instanceName',instanceName)
	
	def set_item_id(self, item_id):
		self.item_id = item_id
	
	def get_item_id(self):
		return self.item_id

	def set_cate_id(self, cate_id):
		self.cate_id = cate_id
	
	def get_cate_id(self):
		return self.cate_id
	
	def set_cust_content(self, cust_content):
		self.cust_content = cust_content
	
	def get_cust_content(self):
		return self.cust_content

	def add_picture(self, pic_name, pic_content):
		encoded_pic_name = base64.b64encode(pic_name)
		encoded_pic_content = base64.b64encode(pic_content)
		self.pic_map[encoded_pic_name] = encoded_pic_content

	# Build Post Content
	def build_post_content(self):
		param_map = {}
		# 参数判断
		if not self.item_id or not self.cate_id or not self.pic_map:
			return False
		# 构建参数
		param_map['item_id'] = self.item_id
		param_map['cat_id'] = self.cate_id
		param_map['cust_content'] = self.cust_content

		# 遍历图片列表
		pic_list_str = ''
		for pic_name in self.pic_map:
			if not pic_name or not self.pic_map[pic_name]:
				return False
			pic_list_str += pic_name + ','
			param_map[pic_name] = self.pic_map[pic_name]
		
		param_map['pic_list'] = pic_list_str[:-1]

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


	