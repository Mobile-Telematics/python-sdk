#utility.py
import requests
from datetime import datetime, timedelta
import datetime


def handle_response(response):
    
    if not response:
        return {
            'error': 'Verify the credential parameters in your request.'
        }
        
    if response.status_code == 200:
        # If it's a 200 OK response
        data = response.json()
        # ... process the data or return it
        return data

    elif response.status_code == 204:
        # No content
        print("No content received from server. Please check your input.")
        return None

    # Handle other common status codes
    elif response.status_code == 400:
        # Bad Request
        print("Bad request. Please check your input parameters.")
        return None
    elif response.status_code == 401:
        # Unauthorized
        print("Unauthorized. Please check your credentials.")
        return None
    elif response.status_code == 403:
        # Forbidden
        print("Access forbidden. You might not have the necessary permissions.")
        return None
    elif response.status_code == 404:
        # Not Found
        print("Resource not found. Please check your input parameters.")
        return None
    elif response.status_code == 500:
        # Internal Server Error
        print("Internal server error. Please try again later.")
        return None
    else:
        print(f"Unexpected response from server with status code: {response.status_code}")
        return None


# You can add other functionalities related to trips here.
def adjust_date_range(start_date=None, end_date=None, start_timestamp=None, end_timestamp=None):
    """Adjusts the date range to a maximum of 14 days."""
    
    adjustment_message = "The specified date range exceeded the 14-day limit. Adjusted to retrieve data for the last 14 days."
    
    if start_date and end_date:
        # Convert date strings to datetime objects
        dt_start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        dt_end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        
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