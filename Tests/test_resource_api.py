import json
from playwright.sync_api import APIResponse
from jsonschema import validate
import schemas

class TestResourceAPI:

    def test_list_resource(self, request_context):
        response = request_context.get("unknown")
        assert response.status == 200
        body = response.json()

        validate(instance=body, schema=schemas.RESOURCE_LIST_SCHEMA)

        # These assertions are for learning purposes:
        assert isinstance(body, dict)
        assert "data" in body
        assert isinstance(body["data"], list)

    def test_single_resource(self, request_context):
        response = request_context.get("unknown/2")
        assert response.status == 200

        body = response.json()
        
        validate(instance=body, schema=schemas.SINGLE_RESOURCE_SCHEMA)

        # These assertions are for learning purposes:
        assert isinstance(body, dict)
        assert "data" in body
        assert isinstance(body["data"], dict)

    # Negative Test
    def test_single_resource_not_found(self, request_context):
        response = request_context.get("unknown/23")
        body = response.json()
        assert response.status == 404
        assert body == {}