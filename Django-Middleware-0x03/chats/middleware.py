# chats/middleware.py

import logging
from datetime import datetime


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
