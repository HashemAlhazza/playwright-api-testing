import json
from playwright.sync_api import APIResponse
from jsonschema import validate
import schemas

class TestRegisterAPI:
    def test_register_successful(self, request_context):
        response: APIResponse = request_context.post("register", data={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })
        assert response.status == 200
        body = response.json()
        assert "id" in body and "token" in body

        validate(instance=body, schema=schemas.SUCCESSFUL_REGISTER_SCHEMA)

    # Negative Test    
    def test_register_unsuccessful(self, request_context):
        response: APIResponse = request_context.post("register", data={
            "email": "eve.holt@reqres.in",
        })
        assert response.status == 400
        body = response.json()
        assert "error" in body
        assert body["error"] == "Missing password"

        validate(instance=body, schema=schemas.UNSUCCESSFUL_REGISTER_SCHEMA)