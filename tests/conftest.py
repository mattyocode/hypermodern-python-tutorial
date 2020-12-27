"""Base pytest fixtures."""
from unittest.mock import Mock

from _pytest.config import Config
import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture to patch requests.get with test mock."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Garth's Banquet",
        "extract": "A small meal eaten from a pair of glasses",
    }
    return mock


def pytest_configure(config: Config) -> None:
    """Marks end to end tests."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
