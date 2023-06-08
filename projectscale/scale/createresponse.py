import requests

def create_nps_response(form_data):
    url = "https://100035.pythonanywhere.com/api/nps_responses_create"

    payload = {
        'template_name': form_data['template_name'],
        'scale_id': form_data['scale_id'],
        'instance_id': form_data['instance_id'],
        'brand_name': form_data['brand_name'],
        'product_name': form_data['product_name'],
        'score': form_data['score'],
        'username': form_data['username'],
    }

    headers = {}
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

    return response.text