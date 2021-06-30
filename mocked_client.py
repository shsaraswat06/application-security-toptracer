import requests

APPLICATION_API_URL = 'http://localhost:5001'


def make_request_to_application():
    """
    Function where the example client makes a request to a protected endpoint for the
    example application located at APPLICATION_API_URL.
    """
    headers = {'source': 'service-4', 'api-token': 'e087861a823cec5b380da7bf0e70da0b'}
    url = f"{APPLICATION_API_URL}/protected_endpoint"
    r = requests.get(url, headers=headers)

    try:
        r.raise_for_status()
        print(f"Request successful. Response was: '{r.json()}'")
    except requests.exceptions.HTTPError as e:
        print(f"Request was not successful. Error was: {e.response.text}")


def add_service():
    """
    Add a service and permissions
    """
    headers = {'source': 'service-1', 'api-token': '3cd2c94e218520695ae0979f245bb587'}
    body = {
        'name': 'service-4',
        'applications': ['application-service-1', 'application-service-2', 'application-service-3']
    }
    url = f"{APPLICATION_API_URL}/add_service"
    r = requests.post(url, headers=headers, json=body)

    try:
        r.raise_for_status()
        print(f"Request successful. Response was: '{r.json()}'")
    except requests.exceptions.HTTPError as e:
        print(f"Request was not successful. Error was: {e.response.text}")


if __name__ == '__main__':
    add_service()
