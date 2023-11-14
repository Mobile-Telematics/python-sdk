#utility.py
import requests
from datetime import datetime, timedelta
import datetime


from functools import wraps
from requests.exceptions import HTTPError

def handle_response(response, response_class=dict):
    if not response:
        return response_class({'error': 'Verify the credential parameters in your request.'})
        
    if response.status_code == 200:
        # If it's a 200 OK response
        data = response.json()
        return data
    elif response.status_code == 204:
        print("No content received from server. Please check your input.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    elif response.status_code == 400:
        print("Bad request. Please check your input parameters.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    elif response.status_code == 401:
        print("Unauthorized. Please check your credentials.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    elif response.status_code == 403:
        print("Access forbidden. You might not have the necessary permissions.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    elif response.status_code == 404:
        print("Resource not found. Please check your input parameters.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    elif response.status_code == 500:
        print("Internal server error. Please try again later.")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })
    else:
        print(f"Unexpected response from server with status code: {response.status_code}")
        return response_class({
            "Result": [],
            "Status": "Error",
            "Title": "Bad Request"
        })

def adjust_date_range(start_date=None, end_date=None, start_timestamp=None, end_timestamp=None):
    """Adjusts the date range to a maximum of 14 days."""
    
    adjustment_message = "The specified date range exceeded the 14-day limit. Adjusted to retrieve data for the last 14 days."
    
    if start_date and end_date:
        # Convert date strings to datetime objects
        try:
            dt_start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            dt_end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            dt_start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
            dt_end = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        
        # Ensure the difference is a maximum of 14 days
        if (dt_end - dt_start).days > 14:
            dt_end = dt_start + datetime.timedelta(days=14)
            print(adjustment_message)
        
        # Convert datetime objects back to date strings
        adjusted_start_date = dt_start.strftime('%Y-%m-%d')
        adjusted_end_date = dt_end.strftime('%Y-%m-%d')
        
        return adjusted_start_date, adjusted_end_date, None, None

    elif start_timestamp and end_timestamp:
        # Convert timestamps to datetime objects
        dt_start = datetime.datetime.fromtimestamp(start_timestamp)
        dt_end = datetime.datetime.fromtimestamp(end_timestamp)
        
        # Ensure the difference is a maximum of 14 days
        if (dt_end - dt_start).days > 14:
            dt_end = dt_start + datetime.timedelta(days=14)
            print(adjustment_message)
        
        # Convert datetime objects back to timestamps
        adjusted_start_timestamp = int(dt_start.timestamp())
        adjusted_end_timestamp = int(dt_end.timestamp())
        
        return None, None, adjusted_start_timestamp, adjusted_end_timestamp

    # Handle case where neither date nor timestamp ranges are provided
    return None, None, None, None