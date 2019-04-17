# encoding:utf-8
import os

from tests import unittest

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.credentials.credentials import EcsRamRoleCredential, AccessKeyCredential


class CredentialsChainTest(unittest.TestCase):

    __name__ = 'CredentialsChainTest'

    def test_ecs_config_with_none(self):
        os.environ.setdefault('ALIBABA_CLOUD_ECS_METADATA', '')
        try:
            AcsClient()
            assert False
        except ClientException as e:
            self.assertEqual('Credentials', e.error_code)
            self.assertEqual('Environment variable ALIBABA_CLOUD_ECS_METADATA cannot be empty.',
                             e.get_error_msg())
        os.environ.pop('ALIBABA_CLOUD_ECS_METADATA')

    def test_ecs_config_with_ecs_meta(self):
        os.environ.setdefault('ALIBABA_CLOUD_ECS_METADATA', 'ecs_meta')
        client = AcsClient()
        self.assertTrue(isinstance(client.credentials, EcsRamRoleCredential))
        os.environ.pop('ALIBABA_CLOUD_ECS_METADATA')

    # test local file config
    def test_local_file_default_config_with_none(self):
        os.environ.setdefault('ALIBABA_CLOUD_CREDENTIALS_FILE', '')
        try:
            AcsClient()
            assert False
        except ClientException as e:
            self.assertEqual('Credentials', e.error_code)
            self.assertEqual('The specified credential file path (%s) is invalid.' %
                             os.environ.get('ALIBABA_CLOUD_CREDENTIALS_FILE'), e.get_error_msg())
        os.environ.pop('ALIBABA_CLOUD_CREDENTIALS_FILE')

    def test_local_file_default_config_with_not_none(self):
        os.environ.setdefault('ALIBABA_CLOUD_CREDENTIALS_FILE',
                              'aliyun-python-sdk-core/tests/.alibabacloud/credentials')
        # test with profile_name
        client1 = AcsClient(profile_name='client1')
        self.assertTrue(isinstance(client1.credentials, EcsRamRoleCredential))
        # test default
        client2 = AcsClient()
        self.assertTrue(isinstance(client2.credentials, AccessKeyCredential))
        os.environ.pop('ALIBABA_CLOUD_CREDENTIALS_FILE')

    def test_local_file_env_config(self):
        pass

    # test env config with all
    def test_env_config(self):
        os.environ.setdefault('ALIBABA_CLOUD_ACCESS_KEY_ID', 'access_key_id')
        os.environ.setdefault('ALIBABA_CLOUD_ACCESS_KEY_SECRET', 'access_key_secret')
        client = AcsClient()
        self.assertTrue(isinstance(client.credentials, AccessKeyCredential))
        os.environ.pop('ALIBABA_CLOUD_ACCESS_KEY_ID')
        os.environ.pop('ALIBABA_CLOUD_ACCESS_KEY_SECRET')

    def test_env_config_with_none(self):
        os.environ.setdefault('ALIBABA_CLOUD_ACCESS_KEY_ID', 'access_key_id')
        os.environ.setdefault('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '')
        try:
            AcsClient()
            assert False
        except ClientException as e:
            self.assertEqual('Credentials', e.error_code)
            self.assertEqual('Environment variable ALIBABA_CLOUD_ACCESS_KEY_SECRET '
                             'cannot be empty.', e.get_error_msg())

        os.environ.pop('ALIBABA_CLOUD_ACCESS_KEY_ID')
        os.environ.pop('ALIBABA_CLOUD_ACCESS_KEY_SECRET')

    # test user config
    def test_user_config_with_none(self):
        try:
            AcsClient(access_key_id='access_key_id')
            assert False
        except ClientException as e:
            self.assertEqual('Credentials', e.error_code)
            self.assertEqual('Param access_key_secret can not be empty.',
                             e.get_error_msg())
