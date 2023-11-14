# trips.py

import requests
from datetime import datetime, timedelta

from .auth import TelematicsAuth
from .core import TelematicsCore
from .utility import handle_response, adjust_date_range
from sentry_sdk import capture_exception
import sentry_sdk
import json
from requests.exceptions import HTTPError


sentry_sdk.init(
    dsn="https://c75b486e9aac4eea913b9ac998e21b53@o303533.ingest.sentry.io/4505555960004609",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


class BaseTrips:
    BASE_URL = "https://api.telematicssdk.com/trips/get/admin/v1"

    def __init__(self, auth_client: TelematicsAuth):
        self.auth_client = auth_client

    def _get_headers(self):
        return {
            'accept': 'application/json',
            'authorization': f'Bearer {self.auth_client.get_access_token()}'
        }


class TripsModule:
    def __init__(self, core: TelematicsCore):
        self.core = core  # Ensuring naming consistency

    @property
    def trips(self):
        return Trips(self.core.auth_client)


class Trips(BaseTrips):
    
    def get_list_trips(self, user_id, 
                        start_date=None, end_date=None, 
                        start_date_timestamp_sec=None, end_date_timestamp_sec=None,
                        include_details=False, include_statistics=False, 
                        include_scores=False, include_related=False, 
                        tags_included=None, tags_included_operator=None,
                        tags_excluded=None, tags_excluded_operator=None, 
                        locale="EN", unit_system="Si", 
                        vehicles=None, sort_by="StartDateUtc_Desc", 
                        limit=None):
        """
        Retrieves trip details for a specific user.
        
        :return: Trip details in JSON format.
        """
        
        # Validate the unit_system input
        if unit_system not in ["Si", "Imperial"]:
            print("[NOTIFICATION] Invalid unit_system provided. Please choose either 'Si' or 'Imperial'. Defaulting to 'Si'.")
            unit_system = "Si"  # defaulting to Si
            
        url = f"{self.BASE_URL}"
        
        payload = {
            "Identifiers": {
                "UserId": user_id
            },
            "IncludeDetails": include_details,
            "IncludeStatistics": include_statistics,
            "IncludeScores": include_scores,
            "IncludeRelated": include_related,
            "Locale": locale,
            "UnitSystem": unit_system
        }

        # Using a separate method to adjust the date range
        adjusted_values = adjust_date_range(start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec)
        start_date, end_date, start_date_timestamp_sec, end_date_timestamp_sec = adjusted_values

        if start_date and end_date:
            payload["StartDate"] = start_date
            payload["EndDate"] = end_date
        elif start_date_timestamp_sec and end_date_timestamp_sec:
            payload["StartDateTimestampSec"] = start_date_timestamp_sec
            payload["EndDateTimestampSec"] = end_date_timestamp_sec

        # Ensure tags_included is a list
        if tags_included is not None and not isinstance(tags_included, list):
            tags_included = [tags_included]

        # Ensure tags_excluded is a list
        if tags_excluded is not None and not isinstance(tags_excluded, list):
            tags_excluded = [tags_excluded]

        # Optional fields are added based on their existence
        self._add_to_payload_if_exists(payload, "TagsIncluded", tags_included)
        self._add_to_payload_if_exists(payload, "TagsIncludedOperator", tags_included_operator)
        self._add_to_payload_if_exists(payload, "TagsExcluded", tags_excluded)
        self._add_to_payload_if_exists(payload, "TagsExcludedOperator", tags_excluded_operator)
        self._add_to_payload_if_exists(payload, "Vehicles", vehicles)
        self._add_to_payload_if_exists(payload, "SortBy", sort_by)

        return self._fetch_trip_details(url, payload, limit)
    
    def get_trip_details(self, trip_id, user_id, 
                       include_details=False, include_statistics=False, 
                       include_scores=False, include_waypoints=False,
                       include_events=False, include_related=True, 
                       locale="EN", unit_system="Si"):
        """
        Retrieves specific trip details by its ID.
        
        :return: Trip details in JSON format.
        """
        
        # Validate the unit_system input
        if unit_system not in ["Si", "Imperial"]:
            print("[NOTIFICATION] Invalid unit_system provided. Please choose either 'Si' or 'Imperial'. Defaulting to 'Si'.")
            unit_system = "Si"  # defaulting to Si
            
        url = f"{self.BASE_URL}/{trip_id}"
        
        payload = {
            "Identifiers": {
                "UserId": user_id
            },
            "IncludeDetails": include_details,
            "IncludeStatistics": include_statistics,
            "IncludeScores": include_scores,
            "IncludeWaypoints": include_waypoints,
            "IncludeEvents": include_events,
            "IncludeRelated": include_related,
            "Locale": locale,
            "UnitSystem": unit_system
        }
        try:
            response = self.auth_client.post_with_retry(url, headers=self._get_headers(), json=payload)
            data = handle_response(response)
            if data is not None:
                return TripsResponse(data)
            return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, TripsResponse) # Pass EngagementResponse as an argument
            return e_response    

    def _fetch_trip_details(self, url, payload, limit=None):
        try:
            if limit:
                payload["Paging"] = {"Count": limit, "IncludePagingInfo": False}
                response = self.auth_client.post_with_retry(url, headers=self._get_headers(), json=payload)
                data = handle_response(response)
                if data is not None:
                    return TripsResponse(data)
                return None

            # Handle pagination if limit is not set
            payload["Paging"] = {"Count": 50, "IncludePagingInfo": True}
            all_trips = []
            current_page = 1

            while True:
                payload["Paging"]["Page"] = current_page
                response = self.auth_client.post_with_retry(url, headers=self._get_headers(), json=payload)
                response.raise_for_status()  # Will raise an error for 4xx and 5xx responses.
                trips_response = TripsResponse(response.json())

                all_trips.extend(trips_response.trips)

                # Additional check: if the fetched trips are less than 50 (page size) or there's no next page, break
                if len(trips_response.trips) < 50 or not trips_response.paging_info.get('HasNextPage'):
                    break

                current_page += 1

            trips_response.data['Result']['Trips'] = all_trips
            return trips_response

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, TripsResponse) # Pass EngagementResponse as an argument
            return e_response

        

    def _add_to_payload_if_exists(self, payload, key, value):
        if value:
            payload[key] = value


class TripsResponse:
    def __init__(self, data):
        self.data = data

    @property
    def result(self):
        return self.data.get('Result', {})
    
    @property
    def trips(self):
        trip = self.data.get('Result', {}).get('Trips', [])
        return trip if isinstance(trip, list) else []
    
    
    @property
    def statistics(self):
        trip = self.data.get('Result', {}).get('Trip', {})
        return trip.get('Statistics', {}) if isinstance(trip, dict) else {}

    
    @property
    def details(self):
        return self.data.get('Result', {}).get('Trip', {}).get('Data', {})

    @property
    def transporttype(self):
        return self.data.get('Result', {}).get('Trip', {}).get('Data', {}).get('TransportType', {})

    @property
    def scores(self):
        scores = self.data.get('Result', {}).get('Trip', {}).get('Scores', {})
        return scores if isinstance(scores, dict) else {}

    @property
    def events(self):
        return self.data.get('Result', {}).get('Trip', {}).get('Events', {})

    @property
    def waypoints(self):
        return self.data.get('Result', {}).get('Trip', {}).get('Waypoints', {})

    @property
    def paging_info(self):
        return self.data.get('Result', {}).get('PagingInfo', {})

    @property
    def status(self):
        return self.data.get('Status',{})
    
    @property
    def datetime(self):
        return self.data.get('Data',{})
    
    @property
    def trip_id(self):
        return self.data.get('Result', {}).get('Id',None)
    
    @property
    def full_response(self):
        return self.data
    
    # @property
    # def print_json(self):
    #     print(json.dumps(self.data, indent=4))
        
    def __str__(self):
        return json.dumps(self.data, indent=4)


    # Add at the bottom of statistics.py
def DamoovAuth(email, password):
    auth_client = TelematicsAuth(email, password)
    return Trips(auth_client)

