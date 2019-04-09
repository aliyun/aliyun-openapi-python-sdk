from tests import unittest

from aliyunsdkcore.acs_exception.error_msg import get_msg


class TestErrorMessage(unittest.TestCase):

    def test_get_msg(self):
        self.assertEqual(get_msg("SDK_INVALID_REGION_ID"), "Can not find endpoint to access.")
