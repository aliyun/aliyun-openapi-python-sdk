from aliyunsdkcore.client import AcsClient

ak = 'test-ak'
secret = 'test-secret'
region = 'test-region'
agent = 'aliyuncli'
max_retry_num = 3


class TestClient:

    def test_client_init(self):
        acs_client = AcsClient(ak, secret, region)
        assert acs_client
        acs_client.set_user_agent(agent)
        acs_client.set_auto_retry(True)
        acs_client.set_max_retry_num(max_retry_num)
        assert acs_client.get_user_agent() == agent
        assert acs_client.get_max_retry_num() == max_retry_num
        assert acs_client.get_access_key() == ak
        assert acs_client.get_access_secret() == secret
        assert acs_client.get_region_id() == region
        assert acs_client.is_auto_retry()
