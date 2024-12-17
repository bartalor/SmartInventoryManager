from django.http import HttpRequest
from SmartInventoryManager.models.user import User

class AuthenticatedRequest(HttpRequest):
    user: User