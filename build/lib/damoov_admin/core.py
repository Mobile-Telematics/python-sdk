#core.py
from .auth import TelematicsAuth

class TelematicsCore:
    def __init__(self, email, password):
        self.auth_client = TelematicsAuth(email, password)