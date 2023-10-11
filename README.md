# Damoov Admin SDK

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
