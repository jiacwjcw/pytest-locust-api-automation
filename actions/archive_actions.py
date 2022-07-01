import allure
import json

from actions import base_actions
from users.user import User


class ArchiveActions(User):
    def __init__(self, open_id: str = None):
        super().__init__()
        self.open_id = open_id
        self.login(self.open_id)

    def login(self, open_id: str = None):
        super().login(open_id)

    @allure.step("GET /archives/:archiveID")
    def get_archive_by_id(self, archive_id="", **kwargs):
        return base_actions.get(f"archives/{archive_id}", headers=self.api_headers)

    @allure.step("POST /archives/:archiveID/view archive viewArchive")
    def view_archive(self, archive_id="", **kwargs):
        return base_actions.post(
            f"archives/{archive_id}/view", headers=self.api_headers, data=json.dumps({})
        )

    @allure.step("PATCH /archives/:archiveID")
    def update_archive(self, archive_id="", payload="", **kwargs):
        return base_actions.patch(
            f"archives/{archive_id}", headers=self.api_headers, data=json.dumps(payload)
        )

    @allure.step("POST /archives/:archiveID/like")
    def like_archive(self, archive_id="", owner_id="", **kwargs):
        return base_actions.post(
            f"archives/{archive_id}/like", headers=self.api_headers, data=json.dumps({"ownerID": owner_id})
        )

    @allure.step("DELETE /archives/:archiveID/like")
    def unlike_archive(self, archive_id="", **kwargs):
        return base_actions.delete(
            f"archives/{archive_id}/like", headers=self.api_headers, stream=True
        )

    @allure.step("DELETE /archives/:archiveID")
    def delete_archive(self, archive_id="", **kwargs):
        return base_actions.delete(
            f"archives/{archive_id}", headers=self.api_headers, stream=True
        )

    @allure.step("PATCH /archives/:archiveID/undelete")
    def undelete_archive(self, archive_id="", **kwargs):
        return base_actions.delete(
            f"archives/{archive_id}/undelete", headers=self.api_headers
        )
