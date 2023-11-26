import json
from wiki_data_source import get_content

def _write_to_file(data, filename='medical.json'):
    filename='./src/data/'+filename
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_medical_content():
    with open('./src/data/medical.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_non_medical_content():
    with open('./src/data/non_medical.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def prepare_data():
    _write_to_file(get_content(number=15,medical=True))
    _write_to_file(data=get_content(number=len(get_medical_content()),medical=False),filename='non_medical.json')
