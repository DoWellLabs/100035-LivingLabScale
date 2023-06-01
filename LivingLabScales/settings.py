import requests
# import json

class Settings:

    
    def retrieve(self):
        """
        Retrieve makes a GET Api call to the Settings Api

        :return: All the setting data in the NPS Scale
        :rtype: json

        """

        url = "https://100035.pythonanywhere.com/api/nps_settings_create/"
        response = requests.get(url)
        # for i in response.json()["data"]["data"]:
        #     return f"scale_id: {i['_id']}"        
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error retrieving data. Status Code: {response.status_code}"
        
    
    def create(self, payload:dict ={}):
        """
        Create a scale with a specific setting

        :param payload: The Data to be created
        :type payload: dict

        :return: The Response to API
        :rtype: json
        
        
        """
        url = "https://100035.pythonanywhere.com/api/nps_settings_create/"
        response = requests.post(url, json=payload)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return f"Error, Invalid Data Provided: {response.status_code}"
        

    def update(self, id: str, payload: dict ={}) -> dict:
        """
        Update Scale through Settings
        """

        url = f"https://100035.pythonanywhere.com/nps-editor/settings/{id}"
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            return response.status_code
        else:
            return f"Error, Invalid Data Provided: {response.status_code}"
        

    def template(self, template_name: str):
        """
        Fetch the settings data for a particular scale using the template/ scale name

        :param template_name: name is the scale name
        :type template_name: str

        :return: The Response to API
        :rtype: dict
        """

        url = f"https://100035.pythonanywhere.com/api/nps_settings/{template_name}"
        response = requests.get(url)      
        if response.status_code == 200:
            return response.json()
        else:
            return f"Scale Does Not Exist. Status Code: {response.status_code}"

        

