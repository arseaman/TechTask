import faker

faker = faker.Faker()

CREATE_USER_PAYLOAD = {
        "user": {
            "login": f"{faker.user_name()}",
            "email": f"{faker.email()}",
            "password": f"{faker.password()}",
        }
    }



