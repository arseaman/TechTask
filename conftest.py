import requests as r
import pytest
import user_test
from user_test import test_create_new_user, test_get_user_info


@pytest.fixture
def new_user():
    new_user = test_create_new_user()
    yield new_user


