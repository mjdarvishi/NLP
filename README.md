# Project step
* Accessing Wikipedia API [*]
    the wiki_data_source file is responsible for geting data from Wikipedia api[*]
* Download example and save them in file or database [*]
* Feature Extraction[*]
* Model Implementation[*]
* Training and Testing[*]
* GitHub Repository. Deployment[*]

# Documentation
this code has 3 part 

* Getting data from wiki and caching them as json. This part is responsible for preparing data for this part i have two class wiki_data_source.py that has some method for getting the list of medical and non medical titles and there is method for getting the page. also data_repository is responsible for saving the content in json file and read them from the json file.

* Training part is responsible for training the model and check new titles. In this file there is two method one of them is responsible for creating model and another one is responsible for checking new title.

* Third part of this project is a flask app for making project web base.

# Running Project
In windows run these commands in rout of project:
* pip install -r requirements.txt
* py .\src\app.py

In Linux base systems:
* pip3 install -r requirements.txt
* python3  ./src/app.py
