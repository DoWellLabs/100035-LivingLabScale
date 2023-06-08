import requests


def create_nps_scale(form_data):
    # Process the form data
    username = form_data['username']
    orientation = form_data['orientation']
    scalecolor = form_data['scalecolor']
    roundcolor = form_data['roundcolor']
    fontcolor = form_data['fontcolor']
    format_type = form_data['format_type']
    no_of_scales = form_data['no_of_scales']
    time = form_data['time']
    name = form_data['name']
    left = form_data['left']
    right = form_data['right']
    center = form_data['center']
    label_images = form_data['label_images']
    fontstyle = form_data['fontstyle']
    emoji_format = form_data['emoji_format']

    # Send the form data to your API or perform further processing

    url = "https://100035.pythonanywhere.com/api/nps_settings_create/"

    payload = {
        "user": True,
        "username": username,
        "orientation": orientation,
        "scalecolor": scalecolor,
        "roundcolor": roundcolor,
        "fontcolor": fontcolor,
        "format": format_type,
        "no_of_scales": no_of_scales,
        "time": time,
        "name": name,
        "left": left,
        "right": right,
        "center": center,
        "label_images": label_images,
        "fontstyle": fontstyle,
        "emoji_format": emoji_format
    }

    headers = {}

    response = requests.post(url, headers=headers, json=payload)

    return response.text
