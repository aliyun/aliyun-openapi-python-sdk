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


class PutMetricsRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Cms', '2016-09-22', 'PutMetrics', 'cms')
        self.set_method('POST')
        self.set_accept_format('json')

    def get_callby_cms_owner(self):
        return self.get_query_params().get('callby_cms_owner')

    def set_callby_cms_owner(self, callby_cms_owner):
        self.add_query_param('callby_cms_owner', callby_cms_owner)

    def get_Project(self):
        return self.get_query_params().get('Project')

    def set_Project(self, Project):
        self.add_query_param('Project', Project)

    def get_Metric(self):
        return self.get_query_params().get('Metric')

    def set_Metric(self, Metric):
        self.add_query_param('Metric', Metric)

    def get_Period(self):
        return self.get_query_params().get('Period')

    def set_Period(self, Period):
        self.add_query_param('Period', Period)

    def get_Data(self):
        return self.get_query_params().get('Data')

    def set_Data(self, Data):
        self.add_query_param('Data', Data)
