# (generated with --quick)

import click.testing
import requests.exceptions
from typing import Any, Type
import unittest.mock

CliRunner: Type[click.testing.CliRunner]
Mock: Type[unittest.mock.Mock]
MockFixture: Any
RequestException: Type[requests.exceptions.RequestException]
click: module
console: module
mock_wikipedia_random_page: Any
pytest: Any
runner: Any
test_main_succeeds_in_production_env: Any

def test_main_fails_on_request_error(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_invokes_requests_get(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_prints_error_message_on_request_error(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_prints_title(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_succeeds(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_uses_en_wikipedia_org(runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock) -> None: ...
def test_main_uses_specified_language(runner: click.testing.CliRunner, mock_wikipedia_random_page: unittest.mock.Mock) -> None: ...
