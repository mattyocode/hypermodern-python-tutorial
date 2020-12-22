from unittest.mock import patch, Mock

import click.testing
import click
import pytest
from requests import RequestException

from hypermodern_python import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Garth's Banquet",
        "extract": "A small meal eaten from a pair of glasses",
    }
    return mock

def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
    assert "Garth's Banquet" in result.output

@patch('requests.get')
def test_error_messgae(mock_get, runner):
    mock_get.side_effect = RequestException('HTTPError!')
    result = runner.invoke(console.main)
    assert result.output == 'Error: HTTPError!\n'
    