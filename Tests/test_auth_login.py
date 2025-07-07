import json
from playwright.sync_api import APIResponse
from jsonschema import validate
import schemas

class TestLoginAPI:
    def test_login_successful(self, request_context):
        response: APIResponse = request_context.post("login", data={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        body = response.json()
        assert response.status == 200
        assert "token" in body

        validate(instance=body, schema=schemas.SUCCESSFUL_LOGIN_SCHEMA)

    # Negative Test    
    def test_login_unsuccessful(self, request_context):
        response: APIResponse = request_context.post("login", data={
            "email": "eve.holt@reqres.in",
        })
        body = response.json()
        assert response.status == 400
        assert "error" in body
        assert body["error"] == "Missing password"

        validate(instance=body, schema=schemas.UNSUCCESSFUL_LOGIN_SCHEMA)
        
    def test_delayed_response(self, request_context):
        response: APIResponse = request_context.get("users?delay=3", timeout=3500)
        assert response.status == 200
        body = response.json()

        validate(instance=body, schema=schemas.DELAYED_RESPONSE_SCHEMA)

        for user in body["data"]:
            assert all(key in user for key in ["id", "email", "first_name", "last_name", "avatar"])