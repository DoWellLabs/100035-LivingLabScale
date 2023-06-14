import requests
def create(json_data):
    url = "https://100035.pythonanywhere.com/api/nps_responses_create"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.json()
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"

def fetch(response_id):
    url = f"https://100035.pythonanywhere.com/api/nps_responses/{response_id}"
    headers = {}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.text
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"

def fetch_all():
    url = "https://100035.pythonanywhere.com/api/nps_responses"
    headers = {}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"

import requests

def get_total_responses(document_number, document_name):
    url = f"https://100035.pythonanywhere.com/api/total_responses/{document_number}/{document_name}"
    headers = {}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any non-successful status code
        return response.text
    except requests.exceptions.RequestException as err:
        # Returns error
        return f"Request Exception: {err}"
    except Exception as err:
        # Handle any other exceptions
        return f"Error: {err}"
