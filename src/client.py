from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from defaults import auth_password, auth_url, auth_username

"""
This file creates an HTTP client from an OpenAPI schema.
I also like using the python requests library when I don't have schema.
I would be loading the schema from a local json file.
You can fetch it from a url as well.
I'm also handling basic auth as part of creating the client.
"""
http_client = RequestsClient()
http_client.set_basic_auth(
    auth_url,
    auth_username,
    auth_password
)


def create_client():
    client = SwaggerClient.from_spec(
        '../spec/gateway_schema.json',
        http_client=http_client,
    )
    return client
