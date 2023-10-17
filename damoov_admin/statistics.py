# statistics.py
import requests
from datetime import datetime, timedelta

from .auth import TelematicsAuth
from .core import TelematicsCore
from .utility import handle_response, adjust_date_range
from requests.exceptions import HTTPError
import json




class BaseStatistics:
    BASE_URL = "https://api.telematicssdk.com/indicators/admin/v2"
    
    def __init__(self, auth_client: TelematicsAuth):
        self.auth_client = auth_client
    
    def _get_headers(self):
        return {
            'accept': 'application/json',
            'authorization': f'Bearer {self.auth_client.get_access_token()}'
        }
        
class StatisticsModule:
    def __init__(self, core: TelematicsCore):
        self.core = core  # Renamed self.code to self.core for clarity
        
    @property
    def Statistics(self):
        return Statistics(self.core.auth_client)



class Statistics(BaseStatistics):
    def user_daily_statistics(self, user_id, start_date, end_date, tag=None):
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values
        url = f"{self.BASE_URL}/Statistics/daily?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        if tag:
            url += f"&Tag={tag}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
        
    def user_daily_ecoscore(self, user_id, start_date, end_date):
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values
        url = f"{self.BASE_URL}/Scores/eco/daily?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

    def user_daily_safetyscore(self, user_id, start_date, end_date, tag=None):
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values
        
        url = f"{self.BASE_URL}/Scores/safety/daily?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        if tag:
            url += f"&Tag={tag}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
    
    def user_accumulated_statistics(self, user_id, start_date, end_date, tag=None):
        url = f"{self.BASE_URL}/Statistics?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        if tag:
            url += f"&Tag={tag}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

    def user_accumulated_ecoscore(self, user_id, start_date, end_date):
        url = f"{self.BASE_URL}/Scores/eco?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
        

    def user_accumulated_safetyscore(self, user_id, start_date, end_date, tag=None):
        url = f"{self.BASE_URL}/Scores/safety?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        if tag:
            url += f"&Tag={tag}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
        
    def entity_accumulated_ecoscore(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Scores/eco/consolidated?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        
        try:    
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
        
    
    def entity_daily_ecoscore(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
        

        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values

        
        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Scores/eco/consolidated/daily?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        try:
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
    
    def entity_daily_statistics(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
        

        # Adjust date range if it exceeds 14 days
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values

        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Statistics/consolidated/daily?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        
        try:    
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response
        

    def entity_safety_score(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
       
        # Adjust date range if it exceeds 14 days
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values        
        
        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Scores/safety/consolidated?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        try:    
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

    def entity_accumulated_statistics(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Statistics/consolidated?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        try:    
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

    def entity_daily_safetyscore(self, start_date, end_date, tag=None, instance_id=None, app_id=None, company_id=None):
        
        adjusted_values = adjust_date_range(start_date, end_date)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values
        
        print(start_date, end_date)

        # Check that exactly one of instance_id, app_id, or company_id is provided
        provided_params = [p for p in [instance_id, app_id, company_id] if p is not None]
        
        if len(provided_params) != 1:
            raise ValueError("Exactly one of 'instance_id', 'app_id', or 'company_id' must be provided.")

        url = f"{self.BASE_URL}/Scores/safety/consolidated/daily?StartDate={start_date}&EndDate={end_date}"

        # Add the provided parameter to the URL
        if instance_id:
            url += f"&InstanceId={instance_id}"
        elif app_id:
            url += f"&AppId={app_id}"
        elif company_id:
            url += f"&CompanyId={company_id}"

        if tag:
            url += f"&Tag={tag}"
        try:    
            response = self.auth_client.session.get(url, headers=self._get_headers())
            if response.status_code == 401:  # Access token expired
                self.auth_client.handle_401()
                response = self.auth_client.session.get(url, headers=self._get_headers())

            response.raise_for_status()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

    def _adjust_date_range(self, start_date_obj, end_date_obj):
        """Adjusts the date range to a maximum of 14 days."""
        date_diff = (end_date_obj - start_date_obj).days
        if date_diff > 14:
            start_date_obj = end_date_obj - timedelta(days=14)
        return start_date_obj, end_date_obj

    def lastupdates(self, user_id):
        url = f"{self.BASE_URL}/Statistics/dates?UserId={user_id}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            # return response.json()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response


    def uniquetags(self, user_id, start_date, end_date):
        url = f"{self.BASE_URL}/Statistics/UniqueTags?UserId={user_id}&StartDate={start_date}&EndDate={end_date}"
        try:
            response = self.auth_client.get_with_retry(url, headers=self._get_headers())
            # return response.json()
            return StatisticsResponse(response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, StatisticsResponse) # Pass EngagementResponse as an argument
            return e_response

class StatisticsResponse:
    def __init__(self, data):
        self.data = data

    @property
    def result(self):
        results = self.data.get('Result', [])
        if isinstance(results, list) and len(results) == 1:
            return results[0]
        return results

    @property
    def status(self):
        return self.data.get('Status',{})

    @property
    def title(self):
        return self.data.get('Title', '')

    @property
    def errors(self):
        return self.data.get('Errors', [])
    
    @property
    def latest_trip_date(self):
        return self.result.get('LatestTripDate', None)

    @property
    def latest_scoring_date(self):
        return self.result.get('LatestScoringDate', None)
    
    @property
    def tags_count(self):
        return self.result.get('UniqueTagsCount', None)
    
    @property
    def tags_list(self):
        return self.result.get('UniqueTagsList', None)
    
    @property
    def full_response(self):
        return self.data
    
    def __str__(self):
        return json.dumps(self.data, indent=4)
    
    # Add at the bottom of statistics.py
def DamoovAuth(email, password):
    auth_client = TelematicsAuth(email, password)
    return Statistics(auth_client)
