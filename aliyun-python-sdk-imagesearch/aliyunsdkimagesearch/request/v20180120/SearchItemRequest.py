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
class SearchItemRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ImageSearch', '2018-01-20', 'SearchItem','imagesearch')
		self.set_uri_pattern('/item/search')
		self.set_method('POST')
		self.set_accept_format('JSON')
		self.start = 0
		self.num = 10
		self.cate_id = ''
		self.search_picture = ''

	def get_instance_name(self):
		return self.get_query_params().get('instanceName')

	def set_instance_name(self,instanceName):
		self.add_query_param('instanceName',instanceName)

	def set_start(self, start):
		self.start = start
	
	def get_start(self):
		return self.start
	
	def set_num(self, num):
		self.num = num
	
	def get_num(self):
		return self.num

	def set_cate_id(self, cate_id):
		self.cate_id = cate_id
	
	def get_cate_id(self):
		return self.cate_id
	
	def set_search_picture(self, search_picture):
		self.search_picture = search_picture

	def get_search_picture(self):
		return self.search_picture

	# Build Post Content
	def build_post_content(self):
		param_map = {}
		# 参数判断
		if not self.search_picture :
			return False
		# 构建参数
		param_map['s'] = str(self.start)
		param_map['n'] = str(self.num)
		if self.cate_id and len(self.cate_id) > 0:
			param_map['cat_id'] = self.cate_id

		encoded_pic_name = base64.b64encode("searchPic")
		encoded_pic_content = base64.b64encode(self.search_picture)

		param_map['pic_list'] = encoded_pic_name
		param_map[encoded_pic_name] = encoded_pic_content

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