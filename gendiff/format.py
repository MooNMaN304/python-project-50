import json


def beatiful_json(answer):
    formatted_string = json.dumps(answer, indent=0)
    cleaned_str = formatted_string.replace('"', '').replace(',', '')
    return cleaned_str
