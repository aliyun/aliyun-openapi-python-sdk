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

"""
SDK exception module.

Created on 6/15/2015

@author: alex
"""

import error_type


class ClientException(Exception):
	"""client exception"""

	def __init__(self, code, msg):
		"""

		:param code: error code
		:param message: error message
		:return:
		"""
		Exception.__init__(self)
		self.__error_type = error_type.ERROR_TYPE_CLIENT
		self.message = msg
		self.error_code = code

	def set_error_code(self, code):
		self.error_code = code

	def set_error_msg(self, msg):
		self.message = msg

	def get_error_type(self):
		return self.__error_type

	def get_error_code(self):
		return self.error_code

	def get_error_msg(self):
		return self.message


class ServerException(Exception):
	"""
	server exception
	"""

	def __init__(self, code, msg):
		Exception.__init__(self)
		self.error_code = code
		self.message = msg
		self.__error_type = error_type.ERROR_TYPE_SERVER

	def set_error_code(self, code):
		self.error_code = code

	def set_error_msg(self, msg):
		self.message = msg

	def get_error_type(self):
		return self.__error_type

	def get_error_code(self):
		return self.error_code

	def get_error_msg(self):
		return self.message
