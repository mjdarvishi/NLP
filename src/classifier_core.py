import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from nltk.stem import PorterStemmer
from data_repository import get_medical_content,get_non_medical_content,prepare_data
from wiki_data_source import get_wikipedia_text
from sklearn.preprocessing import LabelEncoder
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download("stopwords")
prepare_data()

# preparing text for the feature extraction part  including :
# tokenization, lowercase conversion, stopword removal, and stemming
def text_preparing(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    return " ".join(stemmed_tokens)


# medical content
medical_content = [text_preparing(item) for item in  get_medical_content()]
# non medical content
non_medical_content = [text_preparing(item) for item in get_non_medical_content()]
labels = ["Medical"] * len(medical_content) + ["Non-Medical"] * len(non_medical_content)
vectorizer = CountVectorizer()




# feature extraction 
def feature_extraction():
    x = vectorizer.fit_transform(medical_content + non_medical_content)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    return x,y

# check the accuracy
def check_accuracy(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    return accuracy_score(y_test, y_pred),  classification_report(y_test, y_pred,target_names=["Medical", "Non-Medical"],output_dict=True)

# classification with two approach naive_bayes_classifier and logistic_regression_classifier
def classification():
    x,y=feature_extraction()
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=True)
    # Bayes classifier
    naive_bayes_classifier = MultinomialNB()
    naive_bayes_classifier.fit(X_train, y_train)

    # Logistic Regression classifier
    logistic_regression_classifier = LogisticRegression()
    logistic_regression_classifier.fit(X_train, y_train)
    naive_bayes_accuracy, naive_bayes_report = check_accuracy(naive_bayes_classifier, X_test, y_test)
    logistic_regression_accuracy, logistic_regression_report = check_accuracy(naive_bayes_classifier, X_test, y_test)

    return naive_bayes_classifier,naive_bayes_accuracy,naive_bayes_report,logistic_regression_classifier,logistic_regression_accuracy,logistic_regression_report

naive_bayes_classifier,naive_bayes_accuracy,naive_bayes_report,logistic_regression_classifier,logistic_regression_accuracy,logistic_regression_report=classification()

# check new document with navie classifier
def check_with_navie(input):
    model=naive_bayes_classifier
    new_content = get_wikipedia_text(text_preparing(input))
    if new_content ==None:
        return None
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    X_new = vectorizer.transform([new_content])
    predicted_class = model.predict(X_new)[0]
    return label_encoder.inverse_transform([predicted_class])[0]

# check new document with logistic regression classifier
def check_with_logistice(input):
    model=logistic_regression_classifier
    new_content = get_wikipedia_text(text_preparing(input))
    if new_content ==None:
        return None
    X_new = vectorizer.transform([new_content])
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    predicted_class = model.predict(X_new)[0]
    return label_encoder.inverse_transform([predicted_class])[0]