from unittest.mock import patch, Mock

import click.testing
import click
import pytest
from requests import RequestException

from hypermodern_python import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0

# Method to be used to replace requests.get
# def mock_requests_get(*args, **kwargs):
#     class MockResponse:
#         def __init__(self, json_data, status_code):
#             self.json_data = json_data
#             self.status_code = status_code

#         def raise_for_status(self):
#             return RequestException(Mock(status=404), 'not found')

#     return MockResponse(None, 404)

@patch('requests.get')
def test_error_messgae(mock_get, runner):
    mock_get.side_effect = RequestException('HTTPError!')
    result = runner.invoke(console.main)
    assert result.output == 'Error: HTTPError!\n'
    