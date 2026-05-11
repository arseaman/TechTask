import payloads
from endpoints.create_objects import CreateNewObjects
from endpoints.get_objects import GetObject
from endpoints.update_object import UpdateObject
import faker
import allure
import os
from dotenv import load_dotenv
import logging as logs


load_dotenv()
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")


def test_create_new_user():
    logs.info("Initialize methods")
    get_user = GetObject()
    create_user = CreateNewObjects()
    payload = payloads.create_unique_user_payload()

    logs.info("Creating a new user")
    create_user.create_new_user(payload)

    logs.info("Checking if the response status code is 200")
    create_user.check_response_is_200()
    data = create_user.response_json

    logs.info("Initializing headers for GET request with Authorization and User-Token")
    headers_get = {
        "Authorization": f'Token token="{AUTHORIZATION_TOKEN}"',
        "User-Token": data["User-Token"],
    }

    logs.info("Retrieving the user's information using the login and checking user's fields and response status code is 200")
    get_user.get_user_by_login(data["login"], headers_get)
    get_user.check_response_is_200()
    get_user.check_user_fields(payload["user"]["login"], payload["user"]["email"])



@allure.suite("Tests with Users")
@allure.title("Test Update User")
@allure.description("This test updates the user's information (login and email) and checks if the update was successful by retrieving the updated user details.")
def test_update_user_info(new_user):
    update_user = UpdateObject()
    check_updated_field = GetObject()
    login = new_user["login"]
    headers = {
        "Authorization": f'Token token="{AUTHORIZATION_TOKEN}"',
        "User-Token": new_user["User-Token"],
    }
    new_name = faker.Faker().user_name()
    new_email = faker.Faker().email()
    UPDATED_USER_PAYLOAD = {
          "user": {
            "login": new_name,
            "email": new_email
          }
        }
    with allure.step("Updating the user's information with new login and email, and checking if the response status code is 200 with successful update message"):
        update_user.update_user(login, payload=UPDATED_USER_PAYLOAD, headers=headers)
        update_user.check_response_is_200()
        update_user.check_successful_update_message()
    with allure.step("Retrieving the updated user's information and checking if the response status code is 200 and the fields are updated correctly"):
        check_updated_field.get_user_by_login(new_name, headers)
        check_updated_field.check_response_is_200()
        check_updated_field.check_user_fields(new_name, new_email)




