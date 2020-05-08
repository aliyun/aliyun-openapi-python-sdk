# Client

## Using AccessKey call

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

# Create and initialize a AcsClient instance
client = AcsClient(
  '<access_key_id>', # The AccessKey ID of the RAM account
  '<access_secret>', # The AccessKey Secret of the RAM account
  '<region_id>"' # The region ID
)

# Create an API request and set parameters
request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')
# Initiate the request and handle the response or exceptions
response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```

## Use the default credential provider chain

The default credential provider chain looks for available credentials, with following order:

1.System Properties

Look for environment credentials in system properties. If the `alibabacloud.accessKeyId` and `alibabacloud.accessKeyIdSecret` system properties are defined and not empty, the program will use them to create default credentials.

2.Environment Credentials

Look for environment credentials in environment variable. If the `ALIBABA_CLOUD_ACCESS_KEY_ID` and `ALIBABA_CLOUD_ACCESS_KEY_SECRET` environment variables are defined and are not empty, the program will use them to create default credentials.

3.Credentials File

If there is `~/.alibabacloud/credentials default file (Windows shows C:\Users\USER_NAME\.alibabacloud\credentials)`, the program automatically creates credentials with the specified type and name. The default file is not necessarily exist, but a parse error will throw an exception. The name of configuration item is lowercase.This configuration file can be shared between different projects and between different tools. Because it is outside of the project and will not be accidentally committed to the version control. The path to the default file can be modified by defining the `ALIBABA_CLOUD_CREDENTIALS_FILE` environment variable. If not configured, use the default configuration `default`. You can also set the environment variables `ALIBABA_CLOUD_PROFILE` to use the configuration.

```ini
[default]                          # default setting
enable = true                      # Enable，Enabled by default if this option is not present
type = access_key                  # Certification type: access_key
access_key_id = foo                # Key
access_key_secret = bar            # Secret

[client1]                          # configuration that is named as `client1`
type = ecs_ram_role                # Certification type: ecs_ram_role
role_name = EcsRamRoleTest         # Role Name

[client2]                          # configuration that is named as `client2`
enable = false                     # Disable
type = ram_role_arn                # Certification type: ram_role_arn
region_id = cn-test
policy = test                      # optional Specify permissions
access_key_id = foo
access_key_secret = bar
role_arn = role_arn
role_session_name = session_name   # optional

[client3]                          # configuration that is named as `client3`
type = rsa_key_pair                # Certification type: rsa_key_pair
public_key_id = publicKeyId        # Public Key ID
private_key_file = /your/pk.pem    # Private Key file
```

4.Instance RAM Role

If the environment variable `ALIBABA_CLOUD_ECS_METADATA` is defined and not empty, the program will take the value of the environment variable as the role name and request http://100.100.100.200/latest/meta-data/ram/security-credentials/ to get the temporary Security credentials.

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

client = AcsClient(
  '<region_id>"'
)

request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```
