import json
import os

import pytest

from client import FireflyAuthClient


@pytest.mark.integration
def test_farcaster_login_smoke_integration() -> None:
    if os.getenv("RUN_INTEGRATION_TESTS", "").lower() != "true":
        pytest.skip("Set RUN_INTEGRATION_TESTS=true to run integration tests.")

    payload_json = os.getenv("FIREFLY_FARCASTER_LOGIN_PAYLOAD_JSON")
    if not payload_json:
        pytest.skip("Set FIREFLY_FARCASTER_LOGIN_PAYLOAD_JSON with request payload JSON.")

    payload = json.loads(payload_json)
    expected_status = int(os.getenv("FIREFLY_EXPECTED_STATUS", "200"))
    expected_code = os.getenv("FIREFLY_EXPECTED_CODE")
    expected_message = os.getenv("FIREFLY_EXPECTED_MESSAGE")

    client = FireflyAuthClient()
    response = client.farcaster_login(payload)

    assert response.status_code == expected_status
    body = response.json()
    assert isinstance(body, dict)
    assert "code" in body
    assert "message" in body

    if expected_code is not None:
        assert body["code"] == int(expected_code)
    if expected_message is not None:
        assert body["message"] == expected_message
