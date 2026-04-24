from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import requests


@dataclass(slots=True)
class FireflyAuthClient:
    base_url: str = "https://api-dev.firefly.land"
    timeout: int = 10
    session: requests.Session = field(default_factory=requests.Session)

    def farcaster_login(self, payload: dict[str, Any] | None = None) -> requests.Response:
        """Call Farcaster login endpoint with stable default headers."""
        url = f"{self.base_url}/v3/auth/farcaster/login"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        request_payload = payload if payload is not None else {}
        return self.session.post(url, headers=headers, json=request_payload, timeout=self.timeout)
