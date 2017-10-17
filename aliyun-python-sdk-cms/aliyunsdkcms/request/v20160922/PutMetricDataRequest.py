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

import socket
import time
import json
from aliyunsdkcore.request import RpcRequest


class PutMetricDataRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Cms', '2016-09-22', 'PutMetricData', 'cms')
        self.__project = None
        self.__metricName = None
        self.__timestamp = time.time() * 1000
        self.__dimensions = {}
        self.__host = None
        self.__value = None
        self.__metricValues = {}
        self.__data = []
        self.set_accept_format('json')

    def get_query_params(self):
        req_params = RpcRequest.get_query_params(self)
        if req_params is None:
            req_params = {}
        row = {}
        if self.__project is not None:
            row['project'] = self.__project

        if self.__metricName is not None:
            row['metricName'] = self.__metricName

        if self.__timestamp is not None:
            row['timestamp'] = self.__timestamp

        if self.__host is not None:
            self.__dimensions['host'] = self.__host

        if self.__value is not None:
            self.__metricValues['value'] = self.__value

        if self.__dimensions:
            row['dimensions'] = self.__dimensions

        if self.__metricValues:
            row['metricValues'] = self.__metricValues

        if row:
            self.__data = [row]

        req_params['Body'] = json.dumps(self.__data)
        return req_params

    def get_P(self):
        return self.get_Project()

    def set_P(self, P):
        self.set_Project(P)

    def get_M(self):
        return self.get_MetricName()

    def set_M(self, M):
        self.set_MetricName(M)

    def get_T(self):
        return self.get_Timestamp()

    def set_T(self, T):
        self.set_Timestamp(T)

    def get_D(self):
        return self.get_Dimensions()

    def set_D(self, D):
        self.set_Dimensions(D)

    def get_H(self):
        return self.get_Host()

    def set_H(self, isH):
        self.set_Host(isH)

    def get_V(self):
        return self.get_Value()

    def set_V(self, V):
        self.set_Value(V)

    def get_C(self):
        return self.get_MetricValues()

    def set_C(self, C):
        return self.set_MetricValues(C)

    def get_Data(self):
        return self.__data

    def set_Data(self, Data):
        self.__data = Data

    def get_Project(self):
        return self.__project

    def set_Project(self, Project):
        self.__project = Project

    def get_MetricName(self):
        return self.__metricName

    def set_MetricName(self, MetricName):
        self.__metricName = MetricName

    def get_Timestamp(self):
        return self.__timestamp

    def set_Timestamp(self, Timestamp):
        self.__timestamp = Timestamp

    def get_Dimensions(self):
        return self.__dimensions

    def set_Dimensions(self, Dimensions):
        dim = {}
        try:
            dim = json.loads(Dimensions)
        except ValueError, e:
            raise ValueError, 'Dimensions format error. Example:\'{"key":"value"}\''
        self.__dimensions = dim

    def get_Host(self):
        return self.__host

    def set_Host(self, isPutHost):
        if isPutHost:
            self.__host = socket.gethostname()

    def get_Value(self):
        return self.__value

    def set_Value(self, Value):
        self.__value = Value

    def get_MetricValues(self):
        return self.__metricValues

    def set_MetricValues(self, MetricValues):
        values = {}
        try:
            values = json.loads(MetricValues)
        except ValueError, e:
            raise ValueError, 'MetricValues format error. Example:\'{"key":"value"}\''
        self.__metricValues = values
