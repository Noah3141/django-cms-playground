# blog/middleware.py
import logging
import time

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Actions before the view is called
        start_time = time.time()
        logger.info(f"\nReceived request: {request.method} to '{request.path}'")

        response = self.get_response(request)

        # Actions after the response has been sent
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f"Sent response (status: {response.status_code}) in {elapsed_time:.2f} seconds\n")

        return response
