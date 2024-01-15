import json
from wiki_data_source import get_content,get_geographic_title as online_geographic,get_non_geographic_title as online_non_geographic
import os
def _write_to_file(data, filename='geographic.json'):
    filename='./src/data/'+filename
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_geographic_content():
    with open('./src/data/geographic.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_non_geographic_content():
    with open('./src/data/non_geographic.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_non_geographic_title():
    with open('./src/data/non_geographic_title.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_geographic_title():
    with open('./src/data/geographic_title.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(len(data))
    return data

def prepare_data():
    if os.path.isfile('./src/data/non_geographic_title.json')==False:
        _write_to_file(data=online_non_geographic(number=300),filename='non_geographic_title.json')
    if os.path.isfile('./src/data/geographic_title.json')==False:
        _write_to_file(data=online_geographic(number=300),filename='geographic_title.json')
    if os.path.isfile('./src/data/geographic.json')==False:
        _write_to_file(get_content(number=50,geographic=True))
    if os.path.isfile('./src/data/non_geographic.json')==False:
        _write_to_file(data=get_content(number=len(get_geographic_content()),geographic=False),filename='non_geographic.json')
