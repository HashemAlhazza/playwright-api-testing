import json
from playwright.sync_api import APIResponse
from jsonschema import validate
import schemas

class TestUserAPI:

    def test_list_users(self, request_context):
        response = request_context.get("users?page=2")
        assert response.status == 200

        body = response.json()
        assert "data" in body

        validate(instance=body, schema=schemas.LIST_USERS_SCHEMA)

        for user in body["data"]:
            assert all(key in user for key in ["id", "email", "first_name", "last_name", "avatar"])

    def test_single_user(self, request_context):
        response = request_context.get("users/2")
        assert response.status == 200
        data = response.json()
        user_id = data["data"]["id"]
        validate(instance=data, schema=schemas.SINGLE_USER_SCHEMA)

    # Negative Test    
    def test_single_user_not_found(self, request_context):
        response = request_context.get("users/23")
        assert response.status == 404
        assert response.json() == {}

    def test_create(self, request_context):
        response = request_context.post("users", data={
            "name": "Hashem",
            "job": "Tester"
        })
        body = response.json()
        assert response.status == 201
        validate(instance=body, schema=schemas.CREATE_USER_SCHEMA)

        # These assertions are for learning purposes:
        assert isinstance(body, dict)
        assert all(key in body for key in ["name", "job", "id", "createdAt"])

    def test_update_put(self, request_context):
        response = request_context.put("users/2", data={
            "name": "Hashem",
            "job": "Embedded Software Engineer"
        })
        body = response.json()

        validate(instance=body, schema=schemas.UPDATE_USER_SCHEMA)

        # These assertions are for learning purposes:  
        assert response.status == 200
        assert isinstance(body, dict)
        assert all(key in body for key in ["name", "job", "updatedAt"])

    def test_delete_user(self, request_context):
        response: APIResponse = request_context.delete("users/2")
        assert response.status == 204
        assert response.text() == ""





