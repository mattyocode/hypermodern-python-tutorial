import pytest


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Garth's Banquet",
        "extract": "A small meal eaten from a pair of glasses",
    }
    return mock