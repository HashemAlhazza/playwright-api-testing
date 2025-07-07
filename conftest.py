import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def request_context():
    playwright = sync_playwright().start()
    context = playwright.request.new_context(
        base_url="https://reqres.in/api/",
        extra_http_headers={
            "x-api-key": "reqres-free-v1" # Provided by the site
        }
    )
    yield context
    context.dispose()
    playwright.stop()
    