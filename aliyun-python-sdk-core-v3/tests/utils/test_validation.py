from aliyunsdkcore.utils import validation
from aliyunsdkcore.acs_exception.exceptions import ClientException

from tests import unittest


class TestValidation(unittest.TestCase):
    def test_validate_pattern(self):
        with self.assertRaises(ClientException) as e:
            validation.validate_pattern('cn@hangzhou', 'region_id', '^[a-zA-Z0-9_-]+$')
        self.assertEqual(e.exception.error_code, "SDK.InvalidParameter")
        validation.validate_pattern('cn-hangzhou', 'region_id', '^[a-zA-Z0-9_-]+$')
