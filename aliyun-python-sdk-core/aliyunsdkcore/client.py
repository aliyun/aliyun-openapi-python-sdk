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

#coding=utf-8
import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, parent_dir)
from .profile import region_provider
from .acs_exception import exceptions as exs
from .acs_exception import error_code, error_msg
from .http.http_response import HttpResponse
from .request import AcsRequest

"""
Acs default client module.

Created on 6/15/2015

@author: alex
"""

class AcsClient:
	def __init__(self, ak, secret, region_id, auto_retry=True, max_retry_time=3, user_agent=None,port = 80):
		"""
		constructor for AcsClient
		:param ak: String, access key id
		:param secret: String, access key secret
		:param region_id: String, region id
		:param auto_retry: Boolean
		:param max_retry_time: Number
		:return:
		"""
		self.__max_retry_num = max_retry_time
		self.__auto_retry = auto_retry
		self.__ak = ak
		self.__secret = secret
		self.__region_id = region_id
		self.__user_agent = user_agent
		self.__port = port

	def get_region_id(self):
		"""

		:return: String
		"""
		return self.__region_id

	def get_access_key(self):
		"""

		:return: String
		"""
		return self.__ak

	def get_access_secret(self):
		"""

		:return: String
		"""
		return self.__secret

	def is_auto_retry(self):
		"""

		:return:Boolean
		"""
		return self.__auto_retry

	def get_max_retry_num(self):
		"""

		:return: Number
		"""
		return self.__max_retry_num

	def get_user_agent(self):
		return self.__user_agent

	def set_region_id(self, region):
		self.__region_id = region

	def set_access_key(self, ak):
		self.__ak = ak

	def set_access_secret(self, secret):
		self.__secret = secret

	def set_max_retry_num(self, num):
		"""
		set auto retry number
		:param num: Numbers
		:return: None
		"""
		self.__max_retry_num = num

	def set_auto_retry(self, flag):
		"""
		set whether or not the client perform auto-retry
		:param flag: Booleans
		:return: None
		"""
		self.__auto_retry = flag

	def set_user_agent(self, agent):
		"""
		User agent set to client will overwrite the request setting.
		:param agent:
		:return:
		"""
		self.__user_agent = agent

	def do_action(self, acs_request):
		ep = region_provider.find_product_domain(self.get_region_id(), acs_request.get_product())
		if ep is None:
			raise exs.ClientException(error_code.SDK_INVALID_REGION_ID, error_msg.get_msg('SDK_INVALID_REGION_ID'))
		if not isinstance(acs_request, AcsRequest):
			raise exs.ClientException(error_code.SDK_INVALID_REQUEST, error_msg.get_msg('SDK_INVALID_REQUEST'))
		try:
			# style = acs_request.get_style()
			content = acs_request.get_content()
			method = acs_request.get_method()
			header = acs_request.get_signed_header(self.get_region_id(), self.get_access_key(), self.get_access_secret())
			if self.get_user_agent() is not None:
				header['User-Agent'] = self.get_user_agent()
				header['x-sdk-client'] = 'python/2.0.0'
			protocol = acs_request.get_protocol_type()
			prefix = self.__replace_occupied_params(acs_request.get_domain_pattern(),acs_request.get_domain_params())
			url = acs_request.get_url(self.get_region_id(),self.get_access_key(),self.get_access_secret())
			if prefix is None:
				response = HttpResponse(ep, url, method, {} if header is None else header, protocol,content,self.__port)
			else:
				response = HttpResponse(prefix + ',' + ep, url, method, {} if header is None else header, protocol,content,self.__port)
			_header, _body = response.get_response()
			# if _body is None:
			# 	raise exs.ClientException(error_code.SDK_SERVER_UNREACHABLE, error_msg.get_msg('SDK_SERVER_UNREACHABLE'))
			return _body
		except IOError:
			raise exs.ClientException(error_code.SDK_SERVER_UNREACHABLE, error_msg.get_msg('SDK_SERVER_UNREACHABLE'))
		except AttributeError:
			raise exs.ClientException(error_code.SDK_INVALID_REQUEST, error_msg.get_msg('SDK_INVALID_REQUEST'))

	def get_response(self, acs_request):
		ep = region_provider.find_product_domain(self.get_region_id(), acs_request.get_product())
		if ep is None:
			raise exs.ClientException(error_code.SDK_INVALID_REGION_ID, error_msg.get_msg('SDK_INVALID_REGION_ID'))
		if not isinstance(acs_request, AcsRequest):
			raise exs.ClientException(error_code.SDK_INVALID_REQUEST, error_msg.get_msg('SDK_INVALID_REQUEST'))
		try:
			# style = acs_request.get_style()
			content = acs_request.get_content()
			method = acs_request.get_method()
			header = acs_request.get_signed_header(self.get_region_id(), self.get_access_key(), self.get_access_secret())
			if self.get_user_agent() is not None:
				header['User-Agent'] = self.get_user_agent()
				header['x-sdk-client'] = 'python/2.0.0'
			protocol = acs_request.get_protocol_type()
			prefix = self.__replace_occupied_params(acs_request.get_domain_pattern(),acs_request.get_domain_params())
			url = acs_request.get_url(self.get_region_id(),self.get_access_key(),self.get_access_secret())
			if prefix is None:
				_response = HttpResponse(ep, url, method, {} if header is None else header, protocol, content,self.__port)
			else:
				_response = HttpResponse(prefix + ',' + ep, url, method, {} if header is None else header, protocol, content,self.__port)
			return _response.get_response_object()
			
		except IOError:
			raise exs.ClientException(error_code.SDK_SERVER_UNREACHABLE, error_msg.get_msg('SDK_SERVER_UNREACHABLE'))
		except AttributeError:
			raise exs.ClientException(error_code.SDK_INVALID_REQUEST, error_msg.get_msg('SDK_INVALID_REQUEST'))

	def __replace_occupied_params(self, pattern, params):
		if pattern is None:
			return None
		if params is None:
			return pattern
		for (k, v) in params.items():
			target = '[' + k + ']'
			pattern.replace(target, v)
		return pattern
