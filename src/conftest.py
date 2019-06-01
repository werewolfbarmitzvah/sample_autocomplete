import pytest
import logging
import requests
from hamcrest import assert_that, equal_to
from requests import json, delete, HTTPBasicAuth # noqa

from defaults import database_url


"""
This is a test ficture file.
Tests would use this to set up certain conditions.
In this case, this is a sample for making a HTTP
request to a database endpoint to delete a record.
You can use test fixtures for almost anything.
"""


@pytest.fixture()
def delete_previous_db_record():
    request = requests.delete(database_url,
                              data=json.dumps({'search_string: some string'}),
                              headers={'Content-type': 'application/json'},
                              auth=HTTPBasicAuth('username', 'password'))
    logging.info(request.body)
    assert_that(request.status_code, equal_to(200))
