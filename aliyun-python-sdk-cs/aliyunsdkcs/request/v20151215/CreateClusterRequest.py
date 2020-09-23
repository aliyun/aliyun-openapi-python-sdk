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

class CreateClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'CreateCluster')
		self.set_uri_pattern('/clusters')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_private_zone(self):
		return self.get_body_params().get('private_zone')

	def set_private_zone(self,private_zone):
		self.add_body_params('private_zone', private_zone)

	def get_proxy_mode(self):
		return self.get_body_params().get('proxy_mode')

	def set_proxy_mode(self,proxy_mode):
		self.add_body_params('proxy_mode', proxy_mode)

	def get_master_system_disk_category(self):
		return self.get_body_params().get('master_system_disk_category')

	def set_master_system_disk_category(self,master_system_disk_category):
		self.add_body_params('master_system_disk_category', master_system_disk_category)

	def get_master_period(self):
		return self.get_body_params().get('master_period')

	def set_master_period(self,master_period):
		self.add_body_params('master_period', master_period)

	def get_cloud_monitor_flags(self):
		return self.get_body_params().get('cloud_monitor_flags')

	def set_cloud_monitor_flags(self,cloud_monitor_flags):
		self.add_body_params('cloud_monitor_flags', cloud_monitor_flags)

	def get_ssh_flags(self):
		return self.get_body_params().get('ssh_flags')

	def set_ssh_flags(self,ssh_flags):
		self.add_body_params('ssh_flags', ssh_flags)

	def get_security_group_id(self):
		return self.get_body_params().get('security_group_id')

	def set_security_group_id(self,security_group_id):
		self.add_body_params('security_group_id', security_group_id)

	def get_container_cidr(self):
		return self.get_body_params().get('container_cidr')

	def set_container_cidr(self,container_cidr):
		self.add_body_params('container_cidr', container_cidr)

	def get_cluster_type(self):
		return self.get_body_params().get('cluster_type')

	def set_cluster_type(self,cluster_type):
		self.add_body_params('cluster_type', cluster_type)

	def get_endpoint_public_access(self):
		return self.get_body_params().get('endpoint_public_access')

	def set_endpoint_public_access(self,endpoint_public_access):
		self.add_body_params('endpoint_public_access', endpoint_public_access)

	def get_worker_auto_renew(self):
		return self.get_body_params().get('worker_auto_renew')

	def set_worker_auto_renew(self,worker_auto_renew):
		self.add_body_params('worker_auto_renew', worker_auto_renew)

	def get_platform(self):
		return self.get_body_params().get('platform')

	def set_platform(self,platform):
		self.add_body_params('platform', platform)

	def get_service_cidr(self):
		return self.get_body_params().get('service_cidr')

	def set_service_cidr(self,service_cidr):
		self.add_body_params('service_cidr', service_cidr)

	def get_node_port_range(self):
		return self.get_body_params().get('node_port_range')

	def set_node_port_range(self,node_port_range):
		self.add_body_params('node_port_range', node_port_range)

	def get_zone_id(self):
		return self.get_body_params().get('zone_id')

	def set_zone_id(self,zone_id):
		self.add_body_params('zone_id', zone_id)

	def get_login_password(self):
		return self.get_body_params().get('login_password')

	def set_login_password(self,login_password):
		self.add_body_params('login_password', login_password)

	def get_kubernetes_version(self):
		return self.get_body_params().get('kubernetes_version')

	def set_kubernetes_version(self,kubernetes_version):
		self.add_body_params('kubernetes_version', kubernetes_version)

	def get_is_enterprise_security_group(self):
		return self.get_body_params().get('is_enterprise_security_group')

	def set_is_enterprise_security_group(self,is_enterprise_security_group):
		self.add_body_params('is_enterprise_security_group', is_enterprise_security_group)

	def get_master_period_unit(self):
		return self.get_body_params().get('master_period_unit')

	def set_master_period_unit(self,master_period_unit):
		self.add_body_params('master_period_unit', master_period_unit)

	def get_master_system_disk_size(self):
		return self.get_body_params().get('master_system_disk_size')

	def set_master_system_disk_size(self,master_system_disk_size):
		self.add_body_params('master_system_disk_size', master_system_disk_size)

	def get_master_count(self):
		return self.get_body_params().get('master_count')

	def set_master_count(self,master_count):
		self.add_body_params('master_count', master_count)

	def get_num_of_nodes(self):
		return self.get_body_params().get('num_of_nodes')

	def set_num_of_nodes(self,num_of_nodes):
		self.add_body_params('num_of_nodes', num_of_nodes)

	def get_deletion_protection(self):
		return self.get_body_params().get('deletion_protection')

	def set_deletion_protection(self,deletion_protection):
		self.add_body_params('deletion_protection', deletion_protection)

	def get_key_pair(self):
		return self.get_body_params().get('key_pair')

	def set_key_pair(self,key_pair):
		self.add_body_params('key_pair', key_pair)

	def get_master_auto_renew(self):
		return self.get_body_params().get('master_auto_renew')

	def set_master_auto_renew(self,master_auto_renew):
		self.add_body_params('master_auto_renew', master_auto_renew)

	def get_profile(self):
		return self.get_body_params().get('profile')

	def set_profile(self,profile):
		self.add_body_params('profile', profile)

	def get_region_id(self):
		return self.get_body_params().get('region_id')

	def set_region_id(self,region_id):
		self.add_body_params('region_id', region_id)

	def get_snat_entry(self):
		return self.get_body_params().get('snat_entry')

	def set_snat_entry(self,snat_entry):
		self.add_body_params('snat_entry', snat_entry)

	def get_worker_system_disk_category(self):
		return self.get_body_params().get('worker_system_disk_category')

	def set_worker_system_disk_category(self,worker_system_disk_category):
		self.add_body_params('worker_system_disk_category', worker_system_disk_category)

	def get_user_data(self):
		return self.get_body_params().get('user_data')

	def set_user_data(self,user_data):
		self.add_body_params('user_data', user_data)

	def get_worker_period_unit(self):
		return self.get_body_params().get('worker_period_unit')

	def set_worker_period_unit(self,worker_period_unit):
		self.add_body_params('worker_period_unit', worker_period_unit)

	def get_master_instance_charge_type(self):
		return self.get_body_params().get('master_instance_charge_type')

	def set_master_instance_charge_type(self,master_instance_charge_type):
		self.add_body_params('master_instance_charge_type', master_instance_charge_type)

	def get_node_cidr_mask(self):
		return self.get_body_params().get('node_cidr_mask')

	def set_node_cidr_mask(self,node_cidr_mask):
		self.add_body_params('node_cidr_mask', node_cidr_mask)

	def get_worker_auto_renew_period(self):
		return self.get_body_params().get('worker_auto_renew_period')

	def set_worker_auto_renew_period(self,worker_auto_renew_period):
		self.add_body_params('worker_auto_renew_period', worker_auto_renew_period)

	def get_master_auto_renew_period(self):
		return self.get_body_params().get('master_auto_renew_period')

	def set_master_auto_renew_period(self,master_auto_renew_period):
		self.add_body_params('master_auto_renew_period', master_auto_renew_period)

	def get_worker_period(self):
		return self.get_body_params().get('worker_period')

	def set_worker_period(self,worker_period):
		self.add_body_params('worker_period', worker_period)

	def get_timeout_mins(self):
		return self.get_body_params().get('timeout_mins')

	def set_timeout_mins(self,timeout_mins):
		self.add_body_params('timeout_mins', timeout_mins)

	def get_images_id(self):
		return self.get_body_params().get('images_id')

	def set_images_id(self,images_id):
		self.add_body_params('images_id', images_id)

	def get_worker_system_disk_size(self):
		return self.get_body_params().get('worker_system_disk_size')

	def set_worker_system_disk_size(self,worker_system_disk_size):
		self.add_body_params('worker_system_disk_size', worker_system_disk_size)

	def get_vpcid(self):
		return self.get_body_params().get('vpcid')

	def set_vpcid(self,vpcid):
		self.add_body_params('vpcid', vpcid)

	def get_os_type(self):
		return self.get_body_params().get('os_type')

	def set_os_type(self,os_type):
		self.add_body_params('os_type', os_type)

	def get_cpu_policy(self):
		return self.get_body_params().get('cpu_policy')

	def set_cpu_policy(self,cpu_policy):
		self.add_body_params('cpu_policy', cpu_policy)

	def get_name(self):
		return self.get_body_params().get('name')

	def set_name(self,name):
		self.add_body_params('name', name)

	def get_disable_rollback(self):
		return self.get_body_params().get('disable_rollback')

	def set_disable_rollback(self,disable_rollback):
		self.add_body_params('disable_rollback', disable_rollback)

	def get_worker_instance_charge_type(self):
		return self.get_body_params().get('worker_instance_charge_type')

	def set_worker_instance_charge_type(self,worker_instance_charge_type):
		self.add_body_params('worker_instance_charge_type', worker_instance_charge_type)