from rest_framework import status
from rest_framework.response import Response

class TechChatResponse:
    # Requires an HTTP Status Code from DRF and a response formatted in JSON
    # See http://www.django-rest-framework.org/api-guide/status-codes/
    # See https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    # Converts to a DRF Response
    def as_response(self):
        return Response(self.content, status=self.status_code)

INSUFFICIENT_INFORMATION = TechChatResponse(status.HTTP_400_BAD_REQUEST, { 'detail': 'Insufficient information' })
INVALID_CREDENTIALS = TechChatResponse(status.HTTP_401_UNAUTHORIZED, { 'detail': 'The credentials you provided cannot be determined to be authentic' })
SUCCESS = TechChatResponse(status.HTTP_200_OK, { 'detail': 'Success' })
