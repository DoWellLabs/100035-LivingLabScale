import requests

class Response:
    """
    Response(Scale Reports)

    
    """

    def create_report(self, payload: dict):
        """
        Provide a response to a particular scale instance using the corresponding scale details

        :param payload: The Data to be created
        :type payload: dict

        :return: The Response to API
        :rtype: json
        
        """
        url = "https://100035.pythonanywhere.com/api/nps_responses_create"
        response = requests.post(url, json=payload)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return f"Error, Invalid Data Provided: {response.status_code}"
        

    def response(self, id: str):
        """
        Fetch the response data for a single scale from the database 

        :param id: id is the default mongo db _id
        :type id: str

        :return: The Response to API
        :rtype: dict
        """

        url = f"https://100035.pythonanywhere.com/api/nps_responses/{id}"
        response = requests.get(url)      
        if response.status_code == 200:
            return response.json()
        else:
            return f"Response Data Does Not Exist. Status Code: {response.status_code}"
        

    def all_response(self):
        """
        Fetch the response data for all NPS scales

        :return: All the response data in the NPS Scale
        :rtype: dict

        """

        url = "https://100035.pythonanywhere.com/api/nps_responses"
        response = requests.get(url)   
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error retrieving data. Status Code: {response.status_code}"
        

    def generate_dynamic_instances(self, payload: dict):
        """
        Dynamically generate instances

        :param payload: 'scale_id' and "no_of_documents'
        :type payload: dict

        :return: The Response to API
        :rtype: json
        
        """
        url = "https://100035.pythonanywhere.com/api/nps_create_instance"
        response = requests.post(url, json=payload)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return f"Error, Invalid Data Provided: {response.status_code}"

