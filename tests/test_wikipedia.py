"""Test cases for the wikipedia module."""
from unittest.mock import Mock

import click
import pytest

from hypermodern_python import wikipedia


def test_random_page_uses_given_langugae(mock_requests_get: Mock) -> Mock:
    """It selects the specific Wikipedia language edition."""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page_object(mock_requests_get: Mock) -> Mock:
    """It returns an object of type Page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """It raises `ClickException` when validation fails."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
