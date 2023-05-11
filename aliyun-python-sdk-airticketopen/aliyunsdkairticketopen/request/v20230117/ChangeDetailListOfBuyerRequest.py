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

from aliyunsdkcore.request import RoaRequest

class ChangeDetailListOfBuyerRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'airticketOpen', '2023-01-17', 'ChangeDetailListOfBuyer')
		self.set_uri_pattern('/airticket/v1/change/buyer/detail-list')
		self.set_method('GET')

	def get_biz_language(self): # String
		return null().get('biz_language')

	def set_biz_language(self, biz_language):  # String
		null('biz_language', biz_language)
	def get_biz_currency(self): # String
		return null().get('biz_currency')

	def set_biz_currency(self, biz_currency):  # String
		null('biz_currency', biz_currency)
	def get_biz_session_nick(self): # String
		return null().get('biz_session_nick')

	def set_biz_session_nick(self, biz_session_nick):  # String
		null('biz_session_nick', biz_session_nick)
	def get_biz_havana_id(self): # Long
		return null().get('biz_havana_id')

	def set_biz_havana_id(self, biz_havana_id):  # Long
		null('biz_havana_id', biz_havana_id)
	def get_biz_zone_id(self): # String
		return null().get('biz_zone_id')

	def set_biz_zone_id(self, biz_zone_id):  # String
		null('biz_zone_id', biz_zone_id)
	def get_xacsairticketaccesstoken(self): # String
		return self.get_headers().get('x-acs-airticket-access-token')

	def set_xacsairticketaccesstoken(self, xacsairticketaccesstoken):  # String
		self.add_header('x-acs-airticket-access-token', xacsairticketaccesstoken)
	def get_page_index(self): # Integer
		return self.get_query_params().get('page_index')

	def set_page_index(self, page_index):  # Integer
		self.add_query_param('page_index', page_index)
	def get_biz_session_uid(self): # Long
		return null().get('biz_session_uid')

	def set_biz_session_uid(self, biz_session_uid):  # Long
		null('biz_session_uid', biz_session_uid)
	def get_utc_create_begin(self): # Long
		return self.get_query_params().get('utc_create_begin')

	def set_utc_create_begin(self, utc_create_begin):  # Long
		self.add_query_param('utc_create_begin', utc_create_begin)
	def get_utc_create_end(self): # Long
		return self.get_query_params().get('utc_create_end')

	def set_utc_create_end(self, utc_create_end):  # Long
		self.add_query_param('utc_create_end', utc_create_end)
	def get_xacsairticketlanguage(self): # String
		return self.get_headers().get('x-acs-airticket-language')

	def set_xacsairticketlanguage(self, xacsairticketlanguage):  # String
		self.add_header('x-acs-airticket-language', xacsairticketlanguage)
	def get_page_size(self): # Integer
		return self.get_query_params().get('page_size')

	def set_page_size(self, page_size):  # Integer
		self.add_query_param('page_size', page_size)
	def get_biz_app_key(self): # String
		return null().get('biz_app_key')

	def set_biz_app_key(self, biz_app_key):  # String
		null('biz_app_key', biz_app_key)
