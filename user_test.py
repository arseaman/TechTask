import pytest
import payloads
from endpoints.create_objects import CreateNewObjects
from endpoints.get_objects import GetObject
from endpoints.update_object import UpdateObject
import faker
import allure
import os
from dotenv import load_dotenv

load_dotenv()
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")

@allure.suite("Tests with Users")
@allure.title("Test Create New User")
@allure.description("This test attempts to create a new user with valid credentials and checks if the response is successful.")
def test_create_new_user():
    headers = {"Authorization": f'Token token="{AUTHORIZATION_TOKEN}"'}
    payload = payloads.CREATE_USER_PAYLOAD
    with allure.step("Creating a new user with valid credentials"):
        create_user = CreateNewObjects()
        create_user.create_new_user(payload, headers)
    with allure.step("Checking if the response status code is 200"):
        create_user.check_response_is_200()
        data = create_user.response_json

    return data


@allure.suite("Tests with Users")
@allure.title("Test Get User's Info")
@allure.description("This test retrieves the information of a user created in the previous test and checks if the response contains the correct user details.")
def test_get_user_info(new_user):
    get_user = GetObject()
    login = new_user["login"]
    payload = payloads.CREATE_USER_PAYLOAD
    headers_get = {
        "Authorization": f'Token token="{AUTHORIZATION_TOKEN}"',
        "User-Token": new_user["User-Token"],
    }
    with allure.step("Retrieving the user's information using the login and checking if the response status code is 200"):
        get_user.get_user_by_login(login, headers_get)
        get_user.check_response_is_200()
        get_user.check_users_fields(login, payload["user"]["email"])


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
    UPDATE_USER_PAYLOAD = {
          "user": {
            "login": new_name,
            "email": new_email
          }
        }
    with allure.step("Updating the user's information with new login and email, and checking if the response status code is 200 with successful update message"):
        update_user.update_user(login, payload=UPDATE_USER_PAYLOAD, headers=headers)
        update_user.check_response_is_200()
        update_user.check_successful_update_message()
    with allure.step("Retrieving the updated user's information and checking if the response status code is 200 and the fields are updated correctly"):
        check_updated_field.get_user_by_login(new_name, headers)
        check_updated_field.check_response_is_200()
        check_updated_field.check_users_fields(new_name, new_email)




