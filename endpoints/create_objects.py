import requests
from endpoints.base_endpoint import Endpoint
from urls import URLS

class CreateNewObjects(Endpoint):

    def create_new_user(self, payload, headers):
        self.response = requests.post(URLS.BASE_USERS_URL, json=payload, headers=headers)
        self.response_json = self.response.json()
