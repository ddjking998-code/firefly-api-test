# Firefly Farcaster Login API Tests

This project contains offline automated tests for:

- `POST /v3/auth/farcaster/login`

The suite uses mocked HTTP responses, so no real account, signature, or network call is required.

## Setup

```bash
cd firefly_api_tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest -q
```

To run only offline mock tests:

```bash
pytest -q -m "not integration"
```

## Covered scenarios

- Successful login with valid payload
- Missing body / invalid request body
- Invalid signature
- Rate limiting (`429`)
- Response contract validation with JSON Schema

## Extend with more cases

Add new mock payloads/responses in:

- `tests/fixtures.py`
- `tests/schemas.py`

Then add corresponding tests in:

- `tests/test_farcaster_login.py`

## Optional real-environment smoke test

An integration test template is included in `tests/test_farcaster_login_integration.py`.
It is skipped by default and only runs when explicitly enabled.

```bash
export RUN_INTEGRATION_TESTS=true
export FIREFLY_FARCASTER_LOGIN_PAYLOAD_JSON='{"message":"...","signature":"...","nonce":"..."}'
# Optional: default is 200
export FIREFLY_EXPECTED_STATUS=200
# Optional: assert API business fields when provided
# export FIREFLY_EXPECTED_CODE=0
# export FIREFLY_EXPECTED_MESSAGE="ok"
pytest -q -m integration
```
# firefly-api-test
