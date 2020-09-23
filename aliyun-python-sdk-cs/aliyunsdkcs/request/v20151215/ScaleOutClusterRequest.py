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

class ScaleOutClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'ScaleOutCluster')
		self.set_uri_pattern('/api/v2/clusters/[ClusterId]')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_worker_data_disk(self):
		return self.get_body_params().get('worker_data_disk')

	def set_worker_data_disk(self,worker_data_disk):
		self.add_body_params('worker_data_disk', worker_data_disk)

	def get_key_pair(self):
		return self.get_body_params().get('key_pair')

	def set_key_pair(self,key_pair):
		self.add_body_params('key_pair', key_pair)

	def get_count(self):
		return self.get_body_params().get('count')

	def set_count(self,count):
		self.add_body_params('count', count)

	def get_worker_system_disk_category(self):
		return self.get_body_params().get('worker_system_disk_category')

	def set_worker_system_disk_category(self,worker_system_disk_category):
		self.add_body_params('worker_system_disk_category', worker_system_disk_category)

	def get_cloud_monitor_flags(self):
		return self.get_body_params().get('cloud_monitor_flags')

	def set_cloud_monitor_flags(self,cloud_monitor_flags):
		self.add_body_params('cloud_monitor_flags', cloud_monitor_flags)

	def get_ClusterId(self):
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_path_param('ClusterId',ClusterId)

	def get_user_data(self):
		return self.get_body_params().get('user_data')

	def set_user_data(self,user_data):
		self.add_body_params('user_data', user_data)

	def get_worker_period_unit(self):
		return self.get_body_params().get('worker_period_unit')

	def set_worker_period_unit(self,worker_period_unit):
		self.add_body_params('worker_period_unit', worker_period_unit)

	def get_worker_auto_renew(self):
		return self.get_body_params().get('worker_auto_renew')

	def set_worker_auto_renew(self,worker_auto_renew):
		self.add_body_params('worker_auto_renew', worker_auto_renew)

	def get_worker_auto_renew_period(self):
		return self.get_body_params().get('worker_auto_renew_period')

	def set_worker_auto_renew_period(self,worker_auto_renew_period):
		self.add_body_params('worker_auto_renew_period', worker_auto_renew_period)

	def get_worker_period(self):
		return self.get_body_params().get('worker_period')

	def set_worker_period(self,worker_period):
		self.add_body_params('worker_period', worker_period)

	def get_login_password(self):
		return self.get_body_params().get('login_password')

	def set_login_password(self,login_password):
		self.add_body_params('login_password', login_password)

	def get_worker_system_disk_size(self):
		return self.get_body_params().get('worker_system_disk_size')

	def set_worker_system_disk_size(self,worker_system_disk_size):
		self.add_body_params('worker_system_disk_size', worker_system_disk_size)

	def get_cpu_policy(self):
		return self.get_body_params().get('cpu_policy')

	def set_cpu_policy(self,cpu_policy):
		self.add_body_params('cpu_policy', cpu_policy)

	def get_disable_rollback(self):
		return self.get_body_params().get('disable_rollback')

	def set_disable_rollback(self,disable_rollback):
		self.add_body_params('disable_rollback', disable_rollback)

	def get_image_id(self):
		return self.get_body_params().get('image_id')

	def set_image_id(self,image_id):
		self.add_body_params('image_id', image_id)

	def get_worker_instance_charge_type(self):
		return self.get_body_params().get('worker_instance_charge_type')

	def set_worker_instance_charge_type(self,worker_instance_charge_type):
		self.add_body_params('worker_instance_charge_type', worker_instance_charge_type)