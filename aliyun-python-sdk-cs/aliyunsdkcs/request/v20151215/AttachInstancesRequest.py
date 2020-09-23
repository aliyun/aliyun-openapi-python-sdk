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
from aliyunsdkcs.endpoint import endpoint_data

class AttachInstancesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'AttachInstances')
		self.set_uri_pattern('/clusters/[ClusterId]/attach')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_password(self):
		return self.get_body_params().get('password')

	def set_password(self,password):
		self.add_body_params('password', password)

	def get_keep_instance_name(self):
		return self.get_body_params().get('keep_instance_name')

	def set_keep_instance_name(self,keep_instance_name):
		self.add_body_params('keep_instance_name', keep_instance_name)

	def get_key_pair(self):
		return self.get_body_params().get('key_pair')

	def set_key_pair(self,key_pair):
		self.add_body_params('key_pair', key_pair)

	def get_cpu_policy(self):
		return self.get_body_params().get('cpu_policy')

	def set_cpu_policy(self,cpu_policy):
		self.add_body_params('cpu_policy', cpu_policy)

	def get_is_edge_worker(self):
		return self.get_body_params().get('is_edge_worker')

	def set_is_edge_worker(self,is_edge_worker):
		self.add_body_params('is_edge_worker', is_edge_worker)

	def get_ClusterId(self):
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_path_param('ClusterId',ClusterId)

	def get_user_data(self):
		return self.get_body_params().get('user_data')

	def set_user_data(self,user_data):
		self.add_body_params('user_data', user_data)

	def get_image_id(self):
		return self.get_body_params().get('image_id')

	def set_image_id(self,image_id):
		self.add_body_params('image_id', image_id)

	def get_format_disk(self):
		return self.get_body_params().get('format_disk')

	def set_format_disk(self,format_disk):
		self.add_body_params('format_disk', format_disk)

	def get_nodepool_id(self):
		return self.get_body_params().get('nodepool_id')

	def set_nodepool_id(self,nodepool_id):
		self.add_body_params('nodepool_id', nodepool_id)