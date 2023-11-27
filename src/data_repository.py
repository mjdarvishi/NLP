import json
from wiki_data_source import get_content,get_medical_title as online_medical,get_non_medical_title as online_non_medical
import os
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
def get_non_medical_title():
    with open('./src/data/non_medical_title.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_medical_title():
    with open('./src/data/medical_title.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def prepare_data():
    if os.path.isfile('./src/data/non_medical_title.json')==False:
        _write_to_file(data=online_non_medical(number=300),filename='non_medical_title.json')
    if os.path.isfile('./src/data/medical_title.json')==False:
        _write_to_file(data=online_medical(number=300),filename='medical_title.json')
    if os.path.isfile('./src/data/medical.json')==False:
        _write_to_file(get_content(number=50,medical=True))
    if os.path.isfile('./src/data/non_medical.json')==False:
        _write_to_file(data=get_content(number=len(get_medical_content()),medical=False),filename='non_medical.json')
