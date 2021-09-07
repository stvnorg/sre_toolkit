from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

class UnitTest:
    def __init__(self):
        pass

    def get_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"name": "sre-toolkit"}

    def get_password_generator(self):
        response = client.get("/tools/password-generator")
        assert response.status_code == 200
        assert len(response.json()) == 32 and type(response.json()) == str

    def get_epoch_to_utc(self):
        response = client.get("/tools/epoch-to-utc/1630976762")
        assert response.status_code == 200
        assert response.json() == "2021-09-07 01:06:02"

