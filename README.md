
# Damoov-Admin Python SDK for Telematics API and Services

![Damoov Logo](https://www.damoov.com/wp-content/uploads/2022/07/Damoov_logo_BIMI.svg)

**Damoov** is a leading telematics platform leveraging smartphone capabilities to capture and analyze driving behaviors. Our Python SDK is designed to enable developers to easily integrate and harness the power of Damoov's robust telematics data.

---

## Installation

Install the SDK using pip:

```bash
pip install damoov-admin
```

## Features

- **Authentication:** Seamlessly authenticate and manage sessions.
- **Telematics Data Retrieval:** Fetch driving statistics, safety patterns, performance metrics, and more.
- **Error Handling:** Handle errors effectively with descriptive messages.
- **Utility Functions:** Set of helper functions for date and time management.

## Quick Start

[Full Documentation](https://docs.damoov.com/docs/python-sdk)

1. **Authentication:**

   ```python
    from damoov_admin import statistics, trips, users
    email = "" 
    password = ''

    #Generate your admin credential in Datahub (https://docs.damoov.com/docs/datahub)

    data = <module>.DamoovAuth(email=email, password=password)
   ```

## Documentation

Detailed documentation is available at [Developer Portal](https://docs.damoov.com/docs/python-sdk).

## Feedback and Support

If you have any feedback or need support, please contact us at [hellp@damoov.com](mailto:hello@damoov.com).

## License

This SDK is distributed under the [MIT License](https://docs.damoov.com/docs/license).
=======
# python-admin-sdk
Damoov's Python SDK enables seamless integration with our leading telematics platform. Harness the power of smartphones to capture and analyze driving behaviors. This repo provides tools to easily tap into driving insights, safety metrics, and performance data. Drive smarter with Damoov.


# Modules
## Statistics
*** 
The `Statistics` module provides a comprehensive suite of functionalities to gather various statistics data, ranging from daily user scores to unique tags. Below is a breakdown of its methods and their usage:

## 1. Get started

If you haven't already, install the Damoov-Admin SDK for Python.

```curl
pip install damoov-admin
```

Begin by importing the Statistics module and finalizing the authentication process.

```python
from damoov_admin import statistics
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

stats = statistics.DamoovAuth(email=email, password=password)

```

## 2. Methods

#### Syntaxes:

- `user_id`: ID of the user, also known as a DeviceToken
- `start_date`: Start date in format `YYYY-MM-DDTHH:MM:SS`
- `end_date`: End date in format `YYYY-MM-DDTHH:MM:SS`
- `tag` : ['Tag1', '...', 'TagX']

***

### `user_daily_statistics`

Obtain daily statistics of a user.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date in format `YYYY-MM-DDTHH:MM:SS`
- `end_date`: End date in format `YYYY-MM-DDTHH:MM:SS`
- `tag` (optional): Tag to filter

**Example**:

Request:

```python
user_statistics=stats.user_daily_statistics(
        user_id='2948a036-36f8-4f76-babd-0635874aa3er',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
  			tag=['Business', 'Personal']
        )
```

Response: 

```json
{"Result": [
{
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "ReportDate": "2023-09-02T00:00:00",
            "MileageKm": 200.7945138572461,
            "MileageMile": 124.77371091089272,
            "TripsCount": 8,
            "DriverTripsCount": 8,
            "OtherTripsCount": 0,
            "MaxSpeedKmh": 122.29244232177734,
            "MaxSpeedMileh": 75.99252365875243,
            "AverageSpeedKmh": 54.68438828527036,
            "AverageSpeedMileh": 33.980878880466996,
            "TotalSpeedingKm": 12.483415754279346,
            "TotalSpeedingMile": 7.757194549709185,
            "AccelerationsCount": 4,
            "BrakingsCount": 5,
            "CorneringsCount": 4,
            "PhoneUsageDurationMin": 3.5368999999999997,
            "PhoneUsageMileageKm": 2.2573077536862733,
            "PhoneUsageMileageMile": 1.40269103814065,
            "PhoneUsageSpeedingDurationMin": 0.0,
            "PhoneUsageSpeedingMileageKm": 0.0,
            "PhoneUsageSpeedingMileageMile": 0.0,
            "DrivingTime": 186.96666666666667,
            "NightDrivingTime": 0.0,
            "DayDrivingTime": 45.993165254592896,
            "RushHoursDrivingTime": 140.0721311569214,
            "PermissionsLevel": 92,
            "TrustLevel": 92.0
        },
  ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `user_daily_ecoscore`

Retrieve a user's daily ecoscore.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date

**Example**:

Request:

```python
user_statistics=stats.user_daily_ecoscore(
        user_id='2948a036-36f8-4f76-babd-0635874aa3er',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        )
```

Response: 

```json
"Result": [
         {
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "CalcDate": "2023-10-02T00:00:00",
            "EcoScoreFuel": 97.80603418529739,
            "EcoScoreTyres": 100.0,
            "EcoScoreBrakes": 71.24604879817583,
            "EcoScoreDepreciation": 30.066967347066047,
            "EcoScore": 75.74524464826901,
            "PermissionsLevel": 100,
            "TrustLevel": 100.0
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `user_daily_safetyscore`

Get a user's daily safety score.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter

**Example**:

Request:

```python
    user_statistics=stats.user_daily_safetyscore(
        user_id='2948a036-36f8-4f76-babd-0635874aa3er',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        )
```

Response:

```json
"Result": [     
  {
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "AccelerationScore": 78.0,
            "BrakingScore": 80.0,
            "SpeedingScore": 72.0,
            "PhoneUsageScore": 86.0,
            "CorneringScore": 79.0,
            "SafetyScore": 90.0,
            "CalcDate": "2023-10-02T00:00:00",
            "PermissionsLevel": 100,
            "TrustLevel": 100.0
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `user_accumulated_statistics`

Fetch accumulated statistics for a user.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter

**Example**:

Request:

```python
    user_statistics=stats.user_accumulated_statistics(
        user_id='2948a036-36f8-4f76-babd-0635874aa3er',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        )
```

Response:

```json
    "Result": [
        {
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "MileageKm": 2111.0221881212033,
            "MileageMile": 1311.789187698516,
            "TripsCount": 153,
            "DriverTripsCount": 153,
            "OtherTripsCount": 0,
            "MaxSpeedKmh": 122.29244232177734,
            "MaxSpeedMileh": 75.99252365875243,
            "AverageSpeedKmh": 43.86747108399977,
            "AverageSpeedMileh": 27.25924653159745,
            "TotalSpeedingKm": 144.23474761841058,
            "TotalSpeedingMile": 89.6274721700803,
            "AccelerationsCount": 94,
            "BrakingsCount": 78,
            "CorneringsCount": 45,
            "PhoneUsageDurationMin": 20.447583333333334,
            "PhoneUsageMileageKm": 17.025709577441788,
            "PhoneUsageMileageMile": 10.579775931422326,
            "PhoneUsageSpeedingDurationMin": 0.2427833333333333,
            "PhoneUsageSpeedingMileageKm": 0.32201192397028167,
            "PhoneUsageSpeedingMileageMile": 0.20009820955513297,
            "DrivingTime": 3301.6166666666663,
            "NightDrivingTime": 0.0,
            "DayDrivingTime": 1807.0491929650307,
            "RushHoursDrivingTime": 1490.29370367527,
            "PermissionsLevel": 93,
            "TrustLevel": 93.0
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `user_accumulated_ecoscore`

Acquire a user's accumulated ecoscore over a range.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date

**Example**:

Request:

```python
    user_statistics.user_accumulated_ecoscore(
        user_id='2948a036-36f8-4f46-babd-0635870aa7ed',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00'
        )
```

Response:

```json
"Result": [
        {
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "EcoScoreFuel": 97.21532847773788,
            "EcoScoreTyres": 100.0,
            "EcoScoreBrakes": 83.25091485161596,
            "EcoScoreDepreciation": 26.5303907938692,
            "EcoScore": 75.00759345586548,
            "PermissionsLevel": 93,
            "TrustLevel": 93.0
        }
      ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `user_accumulated_safetyscore`

Obtain a user's accumulated safety score.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter

**Example**:

Request:

```python
    user_statistics=stats.user_accumulated_safetyscore(
        user_id='2948a036-36f8-4f76-babd-0635874aa3er',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        tag='')
```

Response:

```json
"Result": [
        {
            "UserId": "2948a036-36f8-4f76-babd-0635874aa3er",
            "InstanceId": "",
            "AppId": "",
            "CompanyId": "",
            "AccelerationScore": 77.625,
            "BrakingScore": 81.96875,
            "SpeedingScore": 70.125,
            "PhoneUsageScore": 86.46875,
            "CorneringScore": 85.71875,
            "SafetyScore": 89.53125,
            "PermissionsLevel": 93,
            "TrustLevel": 93.0
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
```

***

### `entity_accumulated_ecoscore`

Retrieve the accumulated ecoscore for an entity.

**Parameters**:

- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter
- One of the following must be provided: 
  - `instance_id`: Instance ID 
  - `app_id`: Application ID 
  - `company_id`: Company ID

**Example**:

Request:

```python
    instance_statistics=stats.entity_accumulated_ecoscore(
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        instance_id="your_instance_id",

    )
```

Response:

```json
    "Result": {
        "UserId": null,
        "InstanceId": "your_instance_id",
        "AppId": null,
        "CompanyId": null,
        "EcoScoreFuel": 97.52329737487166,
        "EcoScoreTyres": 100.0,
        "EcoScoreBrakes": 75.59935000534821,
        "EcoScoreDepreciation": 44.719564784133794,
        "EcoScore": 80.30344045080935,
        "PermissionsLevel": 94,
        "TrustLevel": 94.0
    },
    "Status": 200,
    "Title": "",
    "Errors": []
```

***

### `entity_daily_statistics`

Fetch daily statistics for an entity.

**Parameters**:

- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter
- One of the following must be provided:
  - `instance_id`: Instance ID 
  - `app_id`: Application ID 
  - `company_id`: Company ID

**Example**:

Request:

```python
company_d_statistics=stats.entity_daily_statistics(
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        company_id='your_company_id'
    )
```

Response:

```json
"Result": [
        {
            "InstanceId": null,
            "AppId": null,
            "CompanyId": "your_company_id",
            "ReportDate": "2023-09-18T00:00:00",
            "RegisteredUsers": 12,
            "ActiveUsers": 282,
            "MileageKm": 25382.13108184097,
            "MileageMile": 15772.456254255985,
            "TripsCount": 1789,
            "DriverTripsCount": 1786,
            "OtherTripsCount": 3,
            "MaxSpeedKmh": 146.1915283203125,
            "MaxSpeedMileh": 90.84341569824218,
            "AverageSpeedKmh": 36.002057830035696,
            "AverageSpeedMileh": 22.371678735584183,
            "TotalSpeedingKm": 560.9847620514762,
            "TotalSpeedingMile": 348.595931138787,
            "AccelerationsCount": 1139,
            "BrakingsCount": 1326,
            "CorneringsCount": 1474,
            "PhoneUsageDurationMin": 3800.4465833333334,
            "PhoneUsageMileageKm": 2284.020002380001,
            "PhoneUsageMileageMile": 1419.290029478932,
            "PhoneUsageSpeedingDurationMin": 12.098366666666667,
            "PhoneUsageSpeedingMileageKm": 10.980101468687467,
            "PhoneUsageSpeedingMileageMile": 6.823035052642389,
            "DrivingTime": 35077.866666666676,
            "NightDrivingTime": 1351.4007195532322,
            "DayDrivingTime": 21381.867682458833,
            "RushHoursDrivingTime": 12418.06661722064,
            "PermissionsLevel": 95,
            "TrustLevel": 95.0
        },
  ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `entity_safety_score`

Obtain safety score for an entity.

**Parameters**:

- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter
- One of the following must be provided:
  - `instance_id`: Instance ID 
  - `app_id`: Application ID 
  - `company_id`: Company ID

**Example**:

Request:

```python
instance_statistics=stats.entity_daily_safetyscore(
        start_date='2023-09-20T00:00:00',
        end_date='2023-10-02T00:00:00',
        app_id="your_app_id",
    )
```

Response:

```json
"Result": [
			{
            "InstanceId": null,
            "AppId": "your_app_id",
            "CompanyId": null,
            "ReportDate": "2023-10-02T00:00:00",
            "AccelerationScore": 76.99007444168734,
            "BrakingScore": 76.41935483870968,
            "SpeedingScore": 90.21339950372209,
            "PhoneUsageScore": 74.04466501240695,
            "CorneringScore": 74.01488833746899,
            "SafetyScore": 83.22332506203475,
            "PermissionsLevel": 95,
            "TrustLevel": 95.0
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `entity_accumulated_statistics`

Get accumulated statistics for an entity.

**Parameters**:

- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter
- One of the following must be provided:
  - `instance_id`: Instance ID 
  - `app_id`: Application ID 
  - `company_id`: Company ID

**Example**:

Request:

```python
    company_statistics=stats.entity_accumulated_statistics(
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        company_id='your_company_id'
    )
```

Response

```json
{
    "Result": {
        "InstanceId": null,
        "AppId": null,
        "CompanyId": "your_company_id",
        "TotalRegisteredUsers": 299,
        "ActiveUsers": 491,
        "MileageKm": 765112.3461886081,
        "MileageMile": 475440.8119216011,
        "TripsCount": 47429,
        "DriverTripsCount": 47200,
        "OtherTripsCount": 229,
        "MaxSpeedKmh": 235.80712890625,
        "MaxSpeedMileh": 146.53054990234375,
        "AverageSpeedKmh": 37.49730203560512,
        "AverageSpeedMileh": 23.300823484925015,
        "TotalSpeedingKm": 18645.076059143215,
        "TotalSpeedingMile": 11586.050263151588,
        "AccelerationsCount": 31278,
        "BrakingsCount": 39863,
        "CorneringsCount": 40161,
        "PhoneUsageDurationMin": 117555.1976166667,
        "PhoneUsageMileageKm": 67128.67055363058,
        "PhoneUsageMileageMile": 41713.75588202606,
        "PhoneUsageSpeedingDurationMin": 347.51840000000016,
        "PhoneUsageSpeedingMileageKm": 357.2293322990894,
        "PhoneUsageSpeedingMileageMile": 221.98230709065405,
        "DrivingTime": 1014552.5333333339,
        "NightDrivingTime": 43901.92194293812,
        "DayDrivingTime": 636574.804801112,
        "RushHoursDrivingTime": 341089.71085665515,
        "PermissionsLevel": 95,
        "TrustLevel": 95.0
    },
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `entity_daily_safetyscore`

Fetch daily safety score for an entity.

**Parameters**:

- `start_date`: Start date
- `end_date`: End date
- `tag` (optional): Tag to filter
- One of the following must be provided:
  - `instance_id`: Instance ID 
  - `app_id`: Application ID 
  - `company_id`: Company ID

**Example**:

Request:

```python
    app_statistics=stats.entity_daily_safetyscore(
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        app_id="your_app_id", 
    )
```

Response:

```json
"Result": [
{
            "InstanceId": null,
            "AppId": "your_app_id",
            "CompanyId": null,
            "ReportDate": "2023-10-02T00:00:00",
            "AccelerationScore": 76.99007444168734,
            "BrakingScore": 76.41935483870968,
            "SpeedingScore": 90.21339950372209,
            "PhoneUsageScore": 74.04466501240695,
            "CorneringScore": 74.01488833746899,
            "SafetyScore": 83.22332506203475,
            "PermissionsLevel": 95,
            "TrustLevel": 95.0
        },
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `lastupdates`

Get the last updates for a user.

**Parameters**:

- `user_id`: ID of the user

**Example**:

Request:

```python
    metadata=stats.lastupdates(
        user_id='2948a036-36f8-4f46-babd-0635870aa7ed'
        )
```

Response:

```json
{
    "Result": [
        {
            "UserId": "your_user_id",
            "InstanceId": "your_instance_id",
            "AppId": "your_app_id",
            "CompanyId": "your_company_id",
            "LatestTripDate": "2023-10-11T14:33:40+01:00",
            "LatestScoringDate": "2023-10-11T00:00:00"
        }
    ],
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `uniquetags`

Obtain unique tags for a user within a specific range.

**Parameters**:

- `user_id`: ID of the user
- `start_date`: Start date
- `end_date`: End date

**Example**:

Request:

```python
   metadata=stats.uniquetags(
        user_id='2948a036-36f8-4f46-babd-0635870aa7ed',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',                                 
    )
```

Response:

```json
{
    "Result": {
        "UniqueTagsCount": 2,
        "UniqueTagsList": [
            "your_tag_1",
            "your_tag_x"
        ]
    },
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

## 4. Note

- In all methods, if there's a `HTTPError`, the error will be printed, and the response will be handled accordingly.
- For daily statistics, scores, and list of trips, the methods automatically modify the requested period to 14 days if the original request spans a period longer than that.

## 5. Response

The `Statistics Response` processes and provides easy access to specific parts of the data returned by the `Statistics` module. Here's a detailed breakdown of its properties and methods:

### `result`

Provides the 'Result' from the response. If the result is a list with a single item, it returns that item. Otherwise, it returns the full list or results.

**Return Type**: `dict` or `list`

***

### `status`

Returns the 'Status' from the response.

**Return Type**: `dict`

***

### `title`

Returns the 'Title' of the response.

**Return Type**: `str`

***

### `errors`

Fetches any 'Errors' from the response.

**Return Type**: `list`

***

### `latest_trip_date`

Provides the 'LatestTripDate' from the result.

**Return Type**: Depends on data (e.g., `str`, `None`)

***

### `latest_scoring_date`

Retrieves the 'LatestScoringDate' from the result.

**Return Type**: Depends on data (e.g., `str`, `None`)

***

### `tags_count`

Gives the 'UniqueTagsCount' from the result.

**Return Type**: Depends on data (e.g., `int`, `None`)

***

### `tags_list`

Fetches the 'UniqueTagsList' from the result.

**Return Type**: Depends on data (e.g., `list`, `None`)

## 5. Usage

After you fetch data using methods from the `Statistics` module, you can pass the returned data to `StatisticsResponse` to further process and easily access specific parts of the response.

```python
# Import and initial initialization

from damoov_admin import statistics
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

stats = statistics.DamoovAuth(email=email, password=password)

# Methods to fetch user statistics and scores
app_statistics=stats.entity_daily_safetyscore(
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',
        app_id="your_app_id", 
    )
  print(app_statistics)
  print(app_statistics.status)
  print(app_statistics.result)
  
  
  metadata=stats.uniquetags(
        user_id='2948a036-36f8-4f46-babd-0635870aa7ed',
        start_date='2023-09-01T00:00:00',
        end_date='2023-10-02T00:00:00',                                 
    )
  print(metadata.tags_list)
  print(metadata.tags_count)
  
  
  metadata=stats.lastupdates(
        user_id='2948a036-36f8-4f46-babd-0635870aa7ed'
        )
  print(metadata.latest_trip_date)
  print(metadata.latest_scoring_date)
```

## Trips
***
The `Trips` module offers a robust set of functionalities designed for efficient trip data management. This encompasses a range of operations from fetching trip details, updating trip

## 1. Get started

If you haven't already, install the Damoov-Admin SDK for Python.

```curl
pip install damoov-admin
```

Begin by importing the User management module and finalizing the authentication process.

```python
from damoov_admin import trips
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

trips_mngt = trips.DamoovAuth(email=email, password=password)

```

## 2. Methods

The `Trips` module offers a robust set of functionalities tailored for managing and fetching trip-related data. Here's a comprehensive breakdown of its methods and their usage:

#### Syntaxes:

- `sort_by`: Sort parameter (e.g., "StartDateUtc, StartDateUtc_Desc").
- `unit_system`: Measurement unit system (e.g., "Si" or "Imperial")
- `user_id`:  ID of the user/ DeviceToken whose trips are to be fetched.
- `start_date`, `end_date`: Date range for the trip in format `YYYY-MM-DDTHH:MM:SS`
- `start_date_timestamp_sec`, `end_date_timestamp_sec`: Alternative date range using timestamps.
- `include_details`: Include detailed trip data, like start, end address, transportation type, and tags
- `include_statistics`: Include statistics related to the trip.
- `include_scores`: Include scores associated with the trip.
- `include_waypoints`: Include per-second GPS waypoints of the trip.
- `include_events`: Include events or incidents associated with the trip.
- `include_related`: Include related trip data, including URI for future get requests.
- `tags_included`: Tags to be included in the filtering.
- `tags_excluded`: Tags to be excluded in the filtering.
- `limit`: Limit the number of trips returned.

***

### `get_list_trips`

Fetches the list of trips for a specific user, with various optional filters to refine the result set.

- **Parameters**:
  - `user_id`: **Required**
  - `start_date`, `end_date`: **Required.** 
  - `start_date_timestamp_sec`, `end_date_timestamp_sec`
  - `include_details`
  - `include_statistics`
  - `include_scores`
  - `include_related`
  - `tags_included`
  - `tags_excluded`:
  - `unit_system`
  - `sort_by`
  - `limit`

**Example**: 

Request

```python
    user_trip_details=trip.get_list_trips(
    user_id='user_id',
    # start_date='2023-09-09', 
    # end_date='2023-10-10', 
    start_date_timestamp_sec=1696704060, 
    end_date_timestamp_sec=1696713840,
    sort_by='StartDateUtc',
    include_details=False, 
    include_statistics=False, 
    include_scores=False, 
    include_related=True, 
    tags_included=None, 
    tags_excluded=None,  
    locale="EN", 
    unit_system="Imperial",
    # limit=3
    )
```

Response

```json
{
    "Result": {
        "Trips": [
            {
                "Id": "trip_id",
                "DateUpdated": "2022-09-10T12:29:25+00:00",
                "Identifiers": {
                    "CompanyId": "company_id",
                    "ApplicationId": "application_id",
                    "InstanceId": "instance_id",
                    "UserId": "user_id"
                },
                "Data": {
                    "StartDate": "2022-09-10T12:20:25+00:00",
                    "EndDate": "2022-09-10T12:29:25+00:00",
                    "UnitSystem": "Imperial",
                    "Addresses": {
                        "Start": {
                            "Full": "102 Beach St, San Francisco, CA 94133-1101, United States",
                            "Parts": {
                                "CountryCode": "USA",
                                "Country": "United States",
                                "County": "San Francisco",
                                "State": "California",
                                "City": "San Francisco",
                                "District": "Fisherman's Wharf",
                                "Street": "Beach St",
                                "House": "102"
                            }
                        },
                        "End": {
                            "Full": "E Beach, San Francisco, CA 94129, United States",
                            "Parts": {
                                "CountryCode": "USA",
                                "Country": "United States",
                                "County": "San Francisco",
                                "State": "California",
                                "City": "San Francisco",
                                "District": "Presidio",
                                "Street": "E Beach"
                            }
                        }
                    },
                    "TransportType": {
                        "Current": "OriginalDriver",
                        "ConfirmNeeded": false
                    },
                    "Tags": []
                },
                "Statistics": {
                    "Mileage": 4.143953744168464,
                    "DurationMinutes": 17.183333333333334,
                    "AccelerationsCount": 0.0,
                    "BrakingsCount": 0.0,
                    "CorneringsCount": 1.0,
                    "TotalSpeedingMileage": 0.0,
                    "MidSpeedingMileage": 0.0,
                    "HighSpeedingMileage": 0.0,
                    "PhoneUsageDurationMinutes": 11.989366666666665,
                    "PhoneUsageMileage": 3.5955679069262994,
                    "PhoneUsageWithSpeedingDurationMinutes": 0.0,
                    "PhoneUsageWithSpeedingMileage": 0.0,
                    "DayHours": 17.233333587646484,
                    "RushHours": 0.0,
                    "NightHours": 0.0,
                    "AverageSpeed": 11.416121791501084,
                    "MaxSpeed": 19.790273235742262
                },
                "Scores": {
                    "Safety": 97.0,
                    "Acceleration": 100.0,
                    "Braking": 100.0,
                    "Cornering": 56.0,
                    "Speeding": 100.0,
                    "PhoneUsage": 40.0,
                    "Eco": 77.0,
                    "EcoBrakes": 100.0,
                    "EcoDepreciation": 25.0,
                    "EcoFuel": 100.0,
                    "EcoTyres": 100.0
                },
                "Related": [
                    {
                        "Type": "Waypoints",
                        "Uri": "https://api.telematicssdk.com/trips/get/admin/v1/trip_id/waypoints"
                    },
                    {
                        "Type": "Trip",
                        "Uri": "https://api.telematicssdk.com/trips/get/v1/trip_id"
                    }
                ]
            }
        ]
    },
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

***

### `get_trip_details`

Retrieves waypoint details of a specific trip by its unique ID.

- **Parameters**:
  - `trip_id`: (Required)
  - `user_id`: (Required)
  - `include_details`: Include detailed trip data.
  - `include_statistics`: Include statistics related to the trip.
  - `include_scores`: Include scores associated with the trip.
  - `include_waypoints`: Include waypoints of the trip.
  - `include_events`: Include events associated with the trip.
  - `include_related`: Include related trip data.
  - `locale`: Locale settings (e.g., "EN").
  - `unit_system`: Measurement unit system (e.g., "Si" or "Imperial").

**Example**:

Request

```python
    trip_details = trip.get_trip_details(
    trip_id="trip_id",
    user_id="user_id",
    include_details=True, 
    include_statistics=True, 
    include_scores=True, 
    include_waypoints=True,
    include_events=True, 
    include_related=True, 
    locale="EN", 
    unit_system="Imperial"
    )
```

Response

```json
{
    "Result": {
        "Trip": {
            "Id": "trip_id",
            "DateUpdated": "2023-10-11T07:34:31+00:00",
            "Identifiers": {
                "CompanyId": "company_id",
                "ApplicationId": "application_id",
                "InstanceId": "instance_id",
                "UserId": "user_id"
            },
            "Data": {
                "StartDate": "2023-10-09T08:19:23+01:00",
                "StartDateUnixMilliseconds": 1696835963000,
                "EndDate": "2023-10-09T08:36:44+01:00",
                "EndDateUnixMilliseconds": 1696837004000,
                "UnitSystem": "Imperial",
                "Addresses": {
                    "Start": {
                        "Full": "Avenida Marechal Gomes da Costa 17, 1800-253 Lisbon, Portugal",
                        "Parts": {
                            "CountryCode": "PRT",
                            "Country": "Portugal",
                            "County": "Lisbon",
                            "City": "Lisbon",
                            "District": "Lisbon",
                            "Street": "Avenida Marechal Gomes da Costa",
                            "House": "17"
                        }
                    },
                    "End": {
                        "Full": "Rua do Arco do Cego 177, 1000-020 Lisbon, Portugal",
                        "Parts": {
                            "CountryCode": "PRT",
                            "Country": "Portugal",
                            "County": "Lisbon",
                            "City": "Lisbon",
                            "District": "Lisbon",
                            "Street": "Rua do Arco do Cego",
                            "House": "177"
                        }
                    }
                },
                "TransportType": {
                    "Current": "OriginalDriver",
                    "ConfirmNeeded": true
                },
                "Tags": []
            },
            "Statistics": {
                "Mileage": 3.111590678261461,
                "DurationMinutes": 17.35,
                "AccelerationsCount": 1.0,
                "BrakingsCount": 0.0,
                "CorneringsCount": 0.0,
                "TotalSpeedingMileage": 0.021650736620396006,
                "MidSpeedingMileage": 0.06389130188092126,
                "HighSpeedingMileage": 0.0,
                "PhoneUsageDurationMinutes": 0.0,
                "PhoneUsageMileage": 0.0,
                "PhoneUsageWithSpeedingDurationMinutes": 0.0,
                "PhoneUsageWithSpeedingMileage": 0.0,
                "DayHours": 0.0,
                "RushHours": 17.270366668701172,
                "NightHours": 0.0,
                "AverageSpeed": 20.500146429454027,
                "MaxSpeed": 47.186389247420195
            },
            "Scores": {
                "Safety": 79.0,
                "Acceleration": 53.0,
                "Braking": 100.0,
                "Cornering": 100.0,
                "Speeding": 48.0,
                "PhoneUsage": 100.0,
                "Eco": 91.0,
                "EcoBrakes": 100.0,
                "EcoDepreciation": 75.0,
                "EcoFuel": 98.94907,
                "EcoTyres": 100.0
            },
              "Waypoints": [
                {
                    "Index": 0,
                    "SecSinceStart": 0,
                    "PointDateUnixMilliseconds": 0,
                    "Lat": 0,
                    "Long": 0,
                    "Speed": 0,
                    "SpeedLimit": 0,
                    "Speeding":status ,
                    "PhoneUsage": true
                }
              ],
            "Events": [
                {
                    "Id": "",
                    "Type": "Acceleration",
                    "Date": "2023-10-09T08:22:10+01:00",
                    "Lat": 38.74998,
                    "Long": -9.10616,
                    "Value": 3.353325366973877
                }
            ],
            "Related": [
                {
                    "Type": "Waypoints",
                    "Uri": "https://api.telematicssdk.com/trips/get/admin/v1/300665e1-e415-46ab-892f-1cd25afd650d/waypoints"
                }
            ]
        }
    },
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

## 3. Note

- In all methods, if there's a `HTTPError`, the error will be printed, and the response will be handled accordingly.
- For daily statistics, scores, and list of trips, the methods automatically modify the requested period to 14 days if the original request spans a period longer than that.

## 4. Response

The `TripsResponse` processes and provides easy access to specific parts of the data returned by the `Trips` module. Here's a detailed breakdown of its properties:

### `result`

Returns the 'Result' part from the response.

**Return Type**: `dict`

***

### `trips`

Provides the list of 'Trip' items from the response. If the result is not a list, an empty list is returned.

**Return Type**: `list`

***

### `statistics`

Provides the 'Statistics' information for a trip.

**Return Type**: `dict`

***

### `details`

Returns the detailed data for the 'Trip'.

**Return Type**: `dict`

***

### `transporttype`

Provides the 'TransportType' information for a trip.

**Return Type**: `dict`

***

### `scores`

Returns the 'Scores' for the trip.

**Return Type**: `dict`

***

### `events`

Provides the 'Events' for the trip.

**Return Type**: `dict`

***

### `waypoints`

Returns the 'Waypoints' for the trip.

**Return Type**: `dict`

***

### `paging_info`

Provides the paging information if available.

**Return Type**: `dict`

***

### `status`

Returns the 'Status' from the response.

**Return Type**: `dict`

***

### `datetime`

Provides the 'Data' (usually representing datetime) from the response.

**Return Type**: `dict`

***

### `trip_id`

Returns the unique ID for the trip.

**Return Type**: Depends on data (e.g., `str`, `None`)

***

## 5. Usage

After making calls to the `Trips` module to retrieve trip-related data, you can pass the returned data to `TripsResponse` to further process and easily access specific parts of the response.

```python
# Import and initial initialization

from damoov_admin import trips
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

trips_mngt = trips.DamoovAuth(email=email, password=password)

# Method to get a list of trips for selected period of time
user_trip_details=trip.get_list_trips(
    user_id='7623f515-b867-4325-bc63-3a0248d4f774',
    # start_date='2023-09-09', 
    # end_date='2023-10-10', 
    start_date_timestamp_sec=1696704060, 
    end_date_timestamp_sec=1696713840,
    sort_by='StartDateUtc',
    tags_included=['Business'],
    include_details=True, 
    include_statistics=True, 
    include_scores=True, 
    include_related=True, 
    locale="EN", 
    unit_system="Imperial", 
    limit=1
    )

print('status: ', user_trip_details.status)
print('details: ', user_trip_details.details)
print('trips: ',user_trip_details.trips)
print('trip id: ',user_trip_details.trip_id)
print('date and time: ', user_trip_details.datetime)
print(user_trip_details.paging_info)
print(user_trip_details) # prints full response in JSON format
    

# Methods to fetch trip details, including waypoints, for a specific trip ID.
trip_details = trip_mngt.get_trip_details(
      trip_id="trip_id",
      user_id="user_id",
      include_details=True, 
      include_statistics=True, 
      include_scores=True, 
      include_waypoints=True,
      include_events=True, 
      include_related=True, 
      locale="EN", 
      unit_system="Imperial"
    )

print(trip_details) # prints full response in JSON format
print('Status: ', trip_details.status)
print('Result: ',trip_details.result)
print('Statistics: ',trip_details.statistics)
print('Scores: ',trip_details.scores)
print('Events: ',trip_details.events)
print('Waypoints: ',trip_details.waypoints)
print('Details: ',trip_details.details)
print('Transportation mode: ',trip_details.transporttype)
 
```

## Users
***
The `Users` module provides a comprehensive suite of functionalities to manage user data effectively, ranging from user creation, updates, to deletions. Below is a breakdown of its methods and their usage:

## 1. Get started

If you haven't already, install the Damoov-Admin SDK for Python.

```curl
pip install damoov-admin
```

Begin by importing the User management module and finalizing the authentication process.

```python
from damoov_admin import users
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

user_mngt = users.DamoovAuth(email=email, password=password)

```

## 2. Methods

#### Syntaxes:

- `instanceid`:  The instance ID for the user.
- `instancekey`:  The instance Key for the user.
- `ClientId`: A unique identifier assigned by the client for the user.
- `FirstName`: First name of the user.
- `LastName`: Last name of the user.
- `Nickname`: Nickname for the user.
- `Phone`: Phone number of the user.
- `Email`: Email address of the user.
- `CreateAccessToken`: If set to True, a user's access token will be created.

***

### `create_user`

Creates a new user based on the given parameters.

**Parameters**

- `instanceid`: **Required.** 
- `instancekey`: **Required.**
- `FirstName`: Optional. 
- `LastName`: Optional. 
- `Nickname`: Optional. 
- `Phone`: Optional. 
- `Email`: Optional.
- `ClientId`: Optional. 
- `CreateAccessToken`: Optional. 

**Example**:

Request:

```python
    new_user=users_mgnt.create_user(
        instanceid='your_instance_id',
        instancekey='your_instance_key',
        FirstName='FirstName',
        LastName='LastName',
        Nickname='Nickname',
        Phone='123456789',
    )
```

Response:

> 📘 DeviceToken is an old name for UserId

```json
{
    "Result": {
        "DeviceToken": "user_devicetoken/userid", // DeviceToekn is the same as UserId
        "AccessToken": null,
        "RefreshToken": null
    },
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

### `update_user`

Updates user details based on the given parameters.

**Parameters**

- `userid`: **Required.** User's unique identifier.
- `ClientId`: Optional. Client ID for the user.
- `FirstName`: Optional. Updated first name of the user.
- `LastName`: Optional. Updated last name of the user.
- `Nickname`: Optional. Updated nickname for the user.
- `Phone`: Optional. Updated phone number of the user.
- `Email`: Optional. Updated email address of the user.

**Example**:

Request:

```python
    user=users_mgnt.update_user(
        userid='User_Id',
        FirstName='Tim',
        LastName='Plumber',
        Nickname='Tim-tim',
        Phone='123456789',
        ClientId='12-34-56789'
    )
```

Response:

```json
{
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

### `delete_user`

**Parameters**:

**Example**:

Request:

```python
delete_user=users_mgnt.delete_user(
        userid='User_devicetoken/userid'
    )
```

Response:

```
{
    "Status": 200,
    "Title": "",
    "Errors": []
}
```

## 3. Note

- In all methods, if there's a HTTPError, the error will be printed, and the response will be handled accordingly.

## 4. Response

The `UsersResponse` class is tailored to process and provide convenient access to specific parts of the data returned from user-related operations. Here's an in-depth breakdown of its properties and methods:

### `devicetoken`

Returns the `DeviceToken` from the response's `Result` section. It provides the device token/ UseId associated with the user.

**Return Type**: Depends on data (e.g., `str`, `None`)

***

### `userid`

Returns the user ID from the response's `Result` section. It provides the device token/ UseId associated with the user.

**Return Type**: Depends on data (e.g., `str`, `None`)

***

### `status`

Extracts the 'Status' of the response. This typically indicates the success or failure of the operation and might contain relevant status codes or messages.

**Return Type**: `dict`

## 5. Usage

After conducting operations related to users, you can pass the returned data to `UsersResponse` to further process and effortlessly access specific parts of the response.

```python
# Import and initial initialization
from damoov_admin import users
email="your_admin_creds@auth.me"
password="YOUR PASSWORD"

user_mngt = users.DamoovAuth(email=email, password=password)

# Use methods to create and manage users
new_user=users.create_user(
        instanceid='your_instance_id',
        instancekey='your_instance_key',,
    )
    print(new_user)
    print(new_user.devicetoken)
    print(new_user.status)
    print(new_user.userid)
 
 user=users_mgnt.update_user(
        userid='User_Id',
        FirstName='Tim',
        LastName='Plumber',
        Nickname='Tim-tim',
        Phone='123456789',
        ClientId='12-34-56789'
    )

    print(user)
    print(user.status)  
```