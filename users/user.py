import requests
import hashlib
import json
import sys

from typing import Dict, Any


class User:
    def __init__(self):
        self.api_host = "https://sta-api.17app.co"
        self.api_headers: Dict[str, Any] = {
            "Content-Type": "application/json",
            "deviceType": "IOS",
            "deviceName": "iPhone",
            "version": "3.143.0",
        }

    def login(self, open_id: str = "", password: str = "00000000"):
        data: Dict[str, Any] = {
            "openID": f"{open_id}",
            "password": f"{hashlib.md5(password.encode()).hexdigest()}",
        }
        r = requests.post(
            f"{self.api_host}/api/v1/auth/loginAction",
            headers=self.api_headers,
            data=json.dumps(data),
        )

        data = json.loads(r.text)["data"]

        if r.status_code != 200 or json.loads(data)["message"] == "password_wrong":
            sys.exit(f"{self.open_id}: login failed, {r.text}")

        json_data = json.loads(r.text)["data"]
        jwt_token = json.loads(json_data)["jwtAccessToken"]
        user_info = json.loads(json_data)["userInfo"]

        self.api_headers["Authorization"] = f"Bearer {jwt_token}"
        self.user_id = user_info["userID"]
        self.room_id = user_info["roomID"]
