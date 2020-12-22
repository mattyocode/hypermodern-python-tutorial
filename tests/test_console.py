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


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Garth's Banquet" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


@patch('requests.get')
def test_error_messgae(mock_get, runner):
    mock_get.side_effect = RequestException('HTTPError!')
    result = runner.invoke(console.main)
    assert result.exit_code == 1
    assert result.output == 'Error: HTTPError!\n'
    