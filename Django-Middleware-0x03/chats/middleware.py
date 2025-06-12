# chats/middleware.py

import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from collections import defaultdict


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler("requests.log")
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user
        path = request.path
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"{timestamp} - User: {user} - Path: {path}"
        self.logger.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hour = datetime.now().hour
        if hour < 18 or hour >= 21:
            return HttpResponseForbidden(
                "Access to the chat is restricted at this time."
            )
        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_by_ip = defaultdict(list)
        self.message_limit = 5
        self.time_window_seconds = 60

    def __call__(self, request):
        ip = self.get_client_ip(request)

        if request.method == "POST" and request.path.startswith("/chats"):
            current_time = time.time()
            recent_requests = [
                t
                for t in self.requests_by_ip[ip]
                if current_time - t < self.time_window_seconds
            ]

            self.requests_by_ip[ip] = recent_requests
            if len(recent_requests) >= self.message_limit:
                return HttpResponseForbidden(
                    "Message rate limit exceeded. Try again later."
                )

            self.requests_by_ip[ip].append(current_time)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
