import requests
from endpoints.base_endpoint import Endpoint
from urls import URLS

class UpdateObject(Endpoint):

    def update_user(self, user_login, payload, headers):
        self.response = requests.put(f"{URLS.BASE_USERS_URL}/{user_login}", json=payload, headers=headers)
        self.response_json = self.response.json()

    def check_successful_update_message(self):
        assert self.response_json["message"] == "User successfully updated."

