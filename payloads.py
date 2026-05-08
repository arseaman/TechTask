import faker

faker = faker.Faker()

def create_unique_user_payload():
    return {
        "user": {
            "login": f"{faker.user_name()}",
            "email": f"{faker.email()}",
            "password": f"{faker.password()}",
        }
    }



