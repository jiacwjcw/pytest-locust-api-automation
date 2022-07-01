from actions.archive_actions import ArchiveActions


def check_field_type_and_exist(f, t) -> bool:
    return f is not None and type(f) == t


def check_error(resp_json: dict={}, code: int=-1, msg: str="", title: str="") -> bool:
    if code != -1:
        assert resp_json["errorCode"] == code
    if msg:
        assert resp_json["errorMessage"] == msg
    if title:
        assert resp_json["errorTitle"] == title


def archive_metadata_check(resp_json):
    assert check_field_type_and_exist(resp_json["archiveID"], str)
    assert check_field_type_and_exist(resp_json["userID"], str)
    assert check_field_type_and_exist(resp_json["streamID"], str)
    assert check_field_type_and_exist(resp_json["caption"], str)
    assert check_field_type_and_exist(resp_json["videoURL"], str)
    assert check_field_type_and_exist(resp_json["coverPhotoURL"], str)

    assert check_field_type_and_exist(resp_json["viewCount"], int)
    assert check_field_type_and_exist(resp_json["likeCount"], int)
    assert check_field_type_and_exist(resp_json["duration"], int)
    assert check_field_type_and_exist(resp_json["createdAt"], int)
    assert check_field_type_and_exist(resp_json["updatedAt"], int)
    assert check_field_type_and_exist(resp_json["isDeleted"], int)

    assert resp_json["userInfo"] is not None

    assert check_field_type_and_exist(resp_json["visibility"], int)
    assert check_field_type_and_exist(resp_json["labels"], list)
    assert check_field_type_and_exist(resp_json["expiredTime"], int)
    assert check_field_type_and_exist(resp_json["state"], int)

    assert check_field_type_and_exist(resp_json["hasLiked"], bool)


def _get_field_value(archive_instance: ArchiveActions, archive_id: str, field: str):
    response = archive_instance.get_archive_by_id(archive_id)
    resp_json = response.json()

    return resp_json[field] if response.status_code == 200 else None


def get_view_count(archive_instance: ArchiveActions, archive_id: str):
    return _get_field_value(archive_instance, archive_id, "viewCount")

def get_like_count(archive_instance: ArchiveActions, archive_id: str):
    return _get_field_value(archive_instance, archive_id, "likeCount")

def get_has_like(archive_instance: ArchiveActions, archive_id: str):
    return _get_field_value(archive_instance, archive_id, "hasLiked")

def get_is_deleted(archive_instance: ArchiveActions, archive_id: str):
    return _get_field_value(archive_instance, archive_id, "isDeleted")