import pytest
from endpoints.create_objects import CreateNewObjects
import payloads

@pytest.fixture
def new_user():
    payload = payloads.create_unique_user_payload()
    create_user = CreateNewObjects()
    create_user.create_new_user(payload)
    create_user.check_response_is_200()
    user_data = create_user.response_json
    user_data["email"] = payload["user"]["email"]
    yield user_data



