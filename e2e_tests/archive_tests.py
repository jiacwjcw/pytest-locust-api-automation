from flask import Response
import pytest
import allure
import time

from common.utils import TestUtility

from actions.archive_actions import ArchiveActions
from e2e_tests.base_tests import *
from e2e_tests.test_data.fixtures import *


data = TestUtility().read_config("test_data.json")
archive = ArchiveActions(data["user1"]["user_info"]["open_id"])


@pytest.mark.teardown
def test_tear_down():
    for a in data["user1"]["archives"]:
        if not (a.get("is_deleted") or a.get("is_dummy_archive")):
            archive.update_archive(a["id"], a["metadata"])


@allure.description("user1 can get user1's archive by archive id")
def test_get_archive_by_id(archive_item):
    response = archive.get_archive_by_id(archive_item["id"])
    resp_json = response.json()

    if archive_item.get("is_deleted") or archive_item.get("is_dummy_archive"):
        assert response.status_code == 420
        check_error(resp_json, 7, f"invalid archiveID: {archive_item['id']}")
    else:
        assert response.status_code == 200
        archive_metadata_check(resp_json)

        assert resp_json["userID"] == data["user1"]["user_info"]["user_id"]


@allure.description("user1 can add user1's archive view count and view count should increase")
def test_view_archive(archive_item):
    view_count = get_view_count(archive, archive_item["id"])
    response = archive.view_archive(archive_item["id"])
    resp_json = response.json()

    if archive_item.get("is_deleted") or archive_item.get("is_dummy_archive"):
        assert response.status_code == 420
        check_error(resp_json, 7, f"invalid archiveID: {archive_item['id']}")
    else:
        assert response.status_code == 200
        assert resp_json == {}
        time.sleep(5.5)
        assert get_view_count(archive, archive_item["id"]) == view_count + 1


@allure.description("user1 can update user1's archive")
def test_update_archive(archive_item, caption, coverPhotoURL, visibility, labels):
    payload = {
        "caption": caption[1],
        "coverPhotoURL": coverPhotoURL[1],
        "visibility": visibility[1],
        "labels": labels[1],
    }
    response = archive.update_archive(archive_item["id"], payload)
    resp_json = response.json()

    if archive_item.get("is_deleted") or archive_item.get("is_dummy_archive"):
        assert response.status_code == 420
        check_error(resp_json, 7, f"invalid archiveID: {archive_item['id']}")
    else:
        if caption[0] == "long_caption":
            assert response.status_code == 420
            check_error(resp_json, 7, "caption too long")
        else:
            assert response.status_code == 200


@allure.description("user1 can like user1's archive")
def test_like_archive(archive_item):
    has_liked = get_has_like(archive, archive_item["id"])
    if not has_liked:
        like_count = get_like_count(archive, archive_item["id"])
        response = archive.like_archive(archive_item["id"], data["user1"]["user_info"]["user_id"])
        resp_json = response.json()

        assert response.status_code == 200
        assert resp_json == {}
        time.sleep(5.5)
        assert get_like_count(archive, archive_item["id"]) == like_count + 1
        assert get_has_like(archive, archive_item["id"]) == True
    else:
        print(f"{archive_item['id']} has already liked")


@allure.description("user1 can unlike user1's archive")
def test_unlike_archive(archive_item):
    has_liked = get_has_like(archive, archive_item["id"])
    if has_liked:
        like_count = get_like_count(archive, archive_item["id"])
        response = archive.unlike_archive(archive_item["id"])

        assert response.status_code == 204
        assert response.text == ""
        time.sleep(5.5)
        assert get_like_count(archive, archive_item["id"]) == like_count - 1
        assert get_has_like(archive, archive_item["id"]) == False
    else:
        print(f"{archive_item['id']} has already unliked")


@allure.description("user1 can delete user1's archive")
def test_delete_archive(archive_item):
    is_deleted = get_is_deleted(archive, archive_item["id"])
    if not is_deleted:
        response = archive.delete_archive(archive_item["id"])

        assert response.status_code == 204
        assert response.text == ""
