# auth.py

import requests
import threading
import json
import os
from requests.exceptions import HTTPError
from .utility import handle_response

class TelematicsAuth:
    BASE_URL = "https://user.telematicssdk.com/v1/Auth"
    LOGIN_ENDPOINT = f"{BASE_URL}/Login"
    REFRESH_ENDPOINT = f"{BASE_URL}/RefreshToken"
    TOKENS_FILE = "tokens.json"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.lock = threading.Lock()
        self.session = requests.Session()  # Create a session instance
        self._load_tokens()

    def _save_tokens(self):
        with open(self.TOKENS_FILE, 'w') as f:
            json.dump({
                "access_token": self.access_token,
                "refresh_token": self.refresh_token
            }, f)

    def _load_tokens(self):
        if os.path.exists(self.TOKENS_FILE):
            with open(self.TOKENS_FILE, 'r') as f:
                tokens = json.load(f)
                self.access_token = tokens.get("access_token")
                self.refresh_token = tokens.get("refresh_token")

    def login(self):
        payload = {
            "LoginFields": f'{{"email":"{self.email}"}}',
            "Password": self.password
        }
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        try:
            response = self.session.post(self.LOGIN_ENDPOINT, json=payload, headers=headers)  # Use session
            response.raise_for_status()
            tokens = response.json().get('Result', {})
            self.access_token = tokens.get('AccessToken', {}).get('Token')
            self.refresh_token = tokens.get('RefreshToken')
            self._save_tokens()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response

    def refresh(self):
        if not self.refresh_token:
            self.login()
            return

        payload = {
            "AccessToken": self.access_token,
            "RefreshToken": self.refresh_token
        }
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        try:
            response = self.session.post(self.REFRESH_ENDPOINT, json=payload, headers=headers)  # Use session
            if response.status_code == 401:
                self.login()
                return
            response.raise_for_status()
            tokens = response.json().get('Result', {})
            self.access_token = tokens.get('AccessToken', {}).get('Token')
            self.refresh_token = tokens.get('RefreshToken')
            self._save_tokens()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response

    def get_access_token(self):
        with self.lock:
            if not self.access_token:
                self.login()
            return self.access_token

    def handle_401(self):
        with self.lock:
            self.refresh()
            
    def get_with_retry(self, url, headers=None):
        """Performs a GET request and retries once if a 401 status is encountered."""
        try:
            response = self.session.get(url, headers=headers)
            if response.status_code == 401:
                self.handle_401()
                updated_headers = headers.copy() if headers else {}
                updated_headers['authorization'] = f'Bearer {self.get_access_token()}'
                response = self.session.get(url, headers=updated_headers)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response
    
    def post_with_retry(self, url, headers=None, json=None, data=None):
        """Performs a POST request and retries once if a 401 status is encountered."""
        try:
            response = self.session.post(url, headers=headers, json=json, data=data)
            if response.status_code == 401:
                self.handle_401()
                updated_headers = headers.copy() if headers else {}
                updated_headers['authorization'] = f'Bearer {self.get_access_token()}'
                response = self.session.post(url, headers=updated_headers, json=json, data=data)
                print(json)
                print(data)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response

    def put_with_retry(self, url, headers=None, json=None, data=None):
        """Performs a PUT request and retries once if a 401 status is encountered."""
        try:
            response = self.session.put(url, headers=headers, json=json, data=data)
            if response.status_code == 401:
                self.handle_401()
                updated_headers = headers.copy() if headers else {}
                updated_headers['authorization'] = f'Bearer {self.get_access_token()}'
                response = self.session.post(url, headers=updated_headers, json=json, data=data)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response
    
    def delete_with_retry(self, url, headers=None, json=None, data=None):
        """Performs a PUT request and retries once if a 401 status is encountered."""
        try:
            response = self.session.delete(url, headers=headers, json=json, data=data)
            if response.status_code == 401:
                self.handle_401()
                updated_headers = headers.copy() if headers else {}
                updated_headers['authorization'] = f'Bearer {self.get_access_token()}'
                response = self.session.post(url, headers=updated_headers, json=json, data=data)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            handle_response(response)
            return response