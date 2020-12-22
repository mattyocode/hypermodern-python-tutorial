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

@patch('requests.get')
def test_error_messgae(mock_get, runner):
    mock_get.side_effect = RequestException('HTTPError!')
    result = runner.invoke(console.main)
    assert result.output == 'Error: HTTPError!\n'
    