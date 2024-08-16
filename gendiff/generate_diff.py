import json


def gen_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    differences = {}
    keys = sorted(set(data1.keys()).union(data2.keys()))
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                differences[key] = data1[key]
            else:
                differences[f'- {key}'] = data1[key]
                differences[f'+ {key}'] = data2[key]
        if key in data1 and key not in data2:
            differences[f'- {key}'] = data1[key]
        if key not in data1 and key in data2:
            differences[f'+ {key}'] = data2[key]
    formatted_string = json.dumps(differences, indent=0)
    cleaned_str = formatted_string.replace('"', '').replace(',', '')
    return cleaned_str
