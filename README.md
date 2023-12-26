# Project step
* Accessing Wikipedia API for getting titles and content of titles[*]
    the wiki_data_source file is responsible for geting data from Wikipedia api[*]
* Download example and save them in file or database[*]
    data_repository_source.py is responsible for this part.
* processing and preparing the text with nltk library[*]
    this part is responsible for: tokenization, lowercase conversion, stopword removal, and stemming. and classifier_core.py is the file which is responsible for.
* Feature Extraction from prepared and processed content[*]
    converts collection of text documents to a matrix of token counts
* Machine Learning Model[*]
    use two aproach for this part: naive_bayes_classifier and logistic_regression_classifier
* Check the Accuracy and Training Report[*]
* GitHub Repository. Deployment[*]

# Documentation
this code has 3 part 

* Getting data from wiki and caching them as json. This part is responsible for preparing data, for this part i have two class wiki_data_source.py that has some method for getting the list of medical and non medical titles and there is method for getting the page. also data_repository is responsible for saving the content in json file and read them from the json file.

* The main part of this assignment is text classifier. classifier_core.py is responsible for this part. In this file i prepare the content. And next from the prepared content feature will be extracted and convert the contents a matrix of token counts. Then use these matrix for classification, two aproach are used for this step  naive_bayes_classifier and logistic_regression_classifier. And finally calculate the accuracy for each aproach and also get the report from them.

* Third part of this project is a flask app for making project web base.

# Running Project
In windows run these commands in rout of project:
* pip install -r requirements.txt
* py .\src\app.py

In Linux base systems:
* pip3 install -r requirements.txt
* python3  ./src/app.py
