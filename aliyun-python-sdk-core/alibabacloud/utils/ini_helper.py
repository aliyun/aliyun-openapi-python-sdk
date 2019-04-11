# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from alibabacloud.exceptions import ClientException
from alibabacloud.vendored import six


# parse ini file
def _parse_nested(config_value):
    parsed = {}
    for line in config_value.splitlines():
        line = line.strip()
        if not line:
            continue
        key, value = line.split('=', 1)
        parsed[key.strip()] = value.strip()
    return parsed


def raw_config_parse(config_filename, parse_subsections=True):
    config = {}
    path = config_filename
    if path is not None:
        path = os.path.expandvars(path)
        path = os.path.expanduser(path)
        if not os.path.isfile(path):
            raise ClientException(
                'The specified credentials file (%s) does not exist.' % path,
            )
        cp = six.moves.configparser.RawConfigParser()
        try:
            cp.read([path])
        except six.moves.configparser.ParsingError:
            raise ClientException(
                'Credentials file (%s) format is incorrect.' % path
            )
        except six.moves.configparser.Error:
            raise ClientException(
                'Cannot read credentials from (%s).' % path
            )
        else:
            for section in cp.sections():
                config[section] = {}
                for option in cp.options(section):

                    config_value = cp.get(section, option)

                    if parse_subsections and config_value.startswith('\n'):
                        try:
                            config_value = _parse_nested(config_value)
                        except ValueError:
                            raise ClientException(
                                'Unable to parse ini file: %s.' % path
                            )
                    config[section][option] = config_value
    return config


def load_config(config_filename):
    parsed = raw_config_parse(config_filename)
    return parsed
