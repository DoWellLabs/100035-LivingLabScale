import requests
import json
def create(payload):
    url = "https://100035.pythonanywhere.com/api/nps_settings_create/"
    headers = {}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.text
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"

def update(payload):
    url = "https://100035.pythonanywhere.com/api/nps_settings_create/"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.text
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"
def fetch(json_data):
    url = "https://100035.pythonanywhere.com/api/nps_settings_create/"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.get(url, headers=headers, data=json.dumps(json_data))
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.text
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"
