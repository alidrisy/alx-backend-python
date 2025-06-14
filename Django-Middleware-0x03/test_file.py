import unittest
import time


class SimpleHttpResponseForbidden:
    def __init__(self, message):
        self.status_code = 403
        self.message = message


def rate_limit_check(
    request, requests_by_ip, message_limit, time_window_seconds, get_client_ip
):
    ip = get_client_ip(request)

    if request["method"] == "POST" and request["path"].startswith("/chats"):
        current_time = time.time()
        recent_requests = [
            t
            for t in requests_by_ip.get(ip, [])
            if current_time - t < time_window_seconds
        ]
        print(requests_by_ip)
        print(recent_requests)

        requests_by_ip[ip] = recent_requests
        print(len(recent_requests))
        print(message_limit)
        if len(recent_requests) >= message_limit:
            print("Message rate limit exceeded. Try again later.")

        requests_by_ip[ip].append(current_time)

    return None  # No rate limit violation


class RateLimitCheckTest(unittest.TestCase):
    def setUp(self):
        self.requests_by_ip = {}
        self.message_limit = 2
        self.time_window_seconds = 10
        self.request = {"method": "POST", "path": "/chats/some-id"}
        self.ip = "192.168.0.1"

    def get_client_ip(self, request):
        return self.ip

    def test_under_limit(self):
        # Should allow the request
        self.requests_by_ip[self.ip] = []
        response = rate_limit_check(
            self.request,
            self.requests_by_ip,
            self.message_limit,
            self.time_window_seconds,
            self.get_client_ip,
        )
        self.assertIsNone(response)
        self.assertEqual(len(self.requests_by_ip[self.ip]), 1)

    def test_over_limit(self):
        # Should block the request
        now = time.time()
        self.requests_by_ip[self.ip] = [now - 1, now - 1.2, now - 2, now - 3]
        response = rate_limit_check(
            self.request,
            self.requests_by_ip,
            self.message_limit,
            self.time_window_seconds,
            self.get_client_ip,
        )
        self.assertIsInstance(response, SimpleHttpResponseForbidden)
        self.assertEqual(response.status_code, 403)

    def test_old_requests_expire(self):
        # Old requests should be ignored
        now = time.time()
        self.requests_by_ip[self.ip] = [now - 20, now - 30]
        response = rate_limit_check(
            self.request,
            self.requests_by_ip,
            self.message_limit,
            self.time_window_seconds,
            self.get_client_ip,
        )
        self.assertIsNone(response)
        self.assertEqual(
            len(self.requests_by_ip[self.ip]), 1
        )  # Only new timestamp added


if __name__ == "__main__":
    unittest.main()
