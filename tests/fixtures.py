SUCCESS_REQUEST = {
    "message": "sample-farcaster-login-message",
    "signature": "0xvalidsignature",
    "nonce": "nonce-001",
}

SUCCESS_RESPONSE = {
    "code": 0,
    "message": "ok",
    "data": {
        "accessToken": "mock-access-token",
        "refreshToken": "mock-refresh-token",
        "user": {
            "fid": 12345,
            "username": "mock_user",
        },
    },
}

MISSING_BODY_RESPONSE = {
    "code": 1001,
    "message": "invalid request body",
    "data": None,
}

INVALID_SIGNATURE_REQUEST = {
    "message": "sample-farcaster-login-message",
    "signature": "0xinvalidsignature",
    "nonce": "nonce-001",
}

INVALID_SIGNATURE_RESPONSE = {
    "code": 2001,
    "message": "invalid signature",
    "data": None,
}

RATE_LIMIT_RESPONSE = {
    "code": 4290,
    "message": "too many requests",
    "data": None,
}
