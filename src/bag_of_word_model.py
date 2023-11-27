import os
import sys
sys.path.insert(1, os.getcwd())
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from wiki_data_source import get_wikipedia_text
from data_repository import get_medical_content,get_non_medical_content,prepare_data

prepare_data()

medical_content = get_medical_content()

non_medical_content = get_non_medical_content()
labels = ["Medical"] * len(medical_content) + ["Non-Medical"] * len(non_medical_content)


vectorizer = CountVectorizer()
def create_model():
    corpus = medical_content + non_medical_content

    X_bow = vectorizer.fit_transform(corpus)

    # Encode labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)

    # Check the unique classes in y
    unique_classes = set(y)
    if len(unique_classes) < 2:
        raise ValueError("At least two classes are needed in the data.")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_bow, y, test_size=0.2, random_state=42)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred, target_names=["Medical", "Non-Medical"],output_dict=True)

    return model,accuracy,classification_rep

main_model,accuracy,classification_rep=create_model()


def check(input):
    model=main_model
    new_content = get_wikipedia_text(input)
    if new_content ==None:
        return None

    # Transform the new content using the same vectorizer
    X_new = vectorizer.transform([new_content])

    # Make predictions using the trained model
    predicted_class = model.predict(X_new)[0]
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    predicted_category = label_encoder.inverse_transform([predicted_class])[0]

    print(f"Predicted Category for '{input}': {predicted_category}")
    return predicted_category