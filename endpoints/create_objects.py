import requests
from endpoints.base_endpoint import Endpoint
from urls import URLS
import os
from dotenv import load_dotenv

load_dotenv()
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")

class CreateNewObjects(Endpoint):
    headers = {"Authorization": f'Token token="{AUTHORIZATION_TOKEN}"'}

    def create_new_user(self, payload, headers=headers):
        self.response = requests.post(URLS.BASE_USERS_URL, json=payload, headers=headers)
        self.response_json = self.response.json()
