import pytest
from common.utils import TestUtility


data = TestUtility().read_config("test_data.json")


@pytest.fixture(params=data["user1"]["archives"])
def archive_item(request):
    return request.param


@pytest.fixture(params=data["metadata"]["caption"].items())
def caption(request):
    return request.param


@pytest.fixture(params=data["metadata"]["coverPhotoURL"].items())
def coverPhotoURL(request):
    return request.param


@pytest.fixture(params=data["metadata"]["visibility"].items())
def visibility(request):
    return request.param


@pytest.fixture(params=data["metadata"]["labels"].items())
def labels(request):
    return request.param
