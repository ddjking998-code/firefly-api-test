import json

import pytest
import responses
from jsonschema import validate

from client import FireflyAuthClient
from tests.fixtures import (
    INVALID_SIGNATURE_REQUEST,
    INVALID_SIGNATURE_RESPONSE,
    MISSING_BODY_RESPONSE,
    RATE_LIMIT_RESPONSE,
    SUCCESS_REQUEST,
    SUCCESS_RESPONSE,
)
from tests.schemas import SUCCESS_LOGIN_RESPONSE_SCHEMA

ENDPOINT = "https://api-dev.firefly.land/v3/auth/farcaster/login"


@responses.activate
def test_login_success() -> None:
    responses.post(ENDPOINT, json=SUCCESS_RESPONSE, status=200)
    client = FireflyAuthClient()

    resp = client.farcaster_login(SUCCESS_REQUEST)

    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["data"]["accessToken"]
    assert len(responses.calls) == 1

    sent_request = responses.calls[0].request
    assert sent_request.headers["accept"] == "application/json"
    assert sent_request.headers["content-type"] == "application/json"
    assert json.loads(sent_request.body.decode("utf-8")) == SUCCESS_REQUEST


@pytest.mark.parametrize(
    ("payload", "status_code", "response_body", "expected_code", "expected_message"),
    [
        ({}, 400, MISSING_BODY_RESPONSE, 1001, "invalid request body"),
        (
            INVALID_SIGNATURE_REQUEST,
            401,
            INVALID_SIGNATURE_RESPONSE,
            2001,
            "invalid signature",
        ),
        (SUCCESS_REQUEST, 429, RATE_LIMIT_RESPONSE, 4290, "too many requests"),
    ],
)
@responses.activate
def test_login_error_scenarios(
    payload: dict,
    status_code: int,
    response_body: dict,
    expected_code: int,
    expected_message: str,
) -> None:
    responses.post(ENDPOINT, json=response_body, status=status_code)
    client = FireflyAuthClient()

    resp = client.farcaster_login(payload)

    assert resp.status_code == status_code
    body = resp.json()
    assert body["code"] == expected_code
    assert body["message"] == expected_message


@responses.activate
def test_login_response_contract() -> None:
    responses.post(ENDPOINT, json=SUCCESS_RESPONSE, status=200)
    client = FireflyAuthClient()

    resp = client.farcaster_login(SUCCESS_REQUEST)

    validate(instance=resp.json(), schema=SUCCESS_LOGIN_RESPONSE_SCHEMA)
