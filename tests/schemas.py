SUCCESS_LOGIN_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["code", "message", "data"],
    "properties": {
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "data": {
            "type": "object",
            "required": ["accessToken", "refreshToken", "user"],
            "properties": {
                "accessToken": {"type": "string", "minLength": 1},
                "refreshToken": {"type": "string", "minLength": 1},
                "user": {
                    "type": "object",
                    "required": ["fid", "username"],
                    "properties": {
                        "fid": {"type": "integer"},
                        "username": {"type": "string", "minLength": 1},
                    },
                    "additionalProperties": True,
                },
            },
            "additionalProperties": True,
        },
    },
    "additionalProperties": True,
}
