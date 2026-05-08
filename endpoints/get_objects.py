import requests
from endpoints.base_endpoint import Endpoint
from urls import URLS

class GetObject(Endpoint):

    def get_user_by_login(self, user_login, headers):
        self.response = requests.get(f"{URLS.BASE_USERS_URL}/{user_login}", headers=headers)
        self.response_json = self.response.json()

    def check_user_fields(self, login, email):
        assert self.response_json['login'] == login
        assert self.response_json["account_details"]['email'] == email

