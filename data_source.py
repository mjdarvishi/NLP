import wikipedia

def is_medical_document(text):
    medical_annotation = 'Medical'
    return medical_annotation in text

def get_wikipedia_text(page_title):
    try:
        page = wikipedia.page(page_title)
        text = page.content

        if is_medical_document(text):
            print(f"The document '{page_title}' is identified as a medical document.")
        else:
            print(f"The document '{page_title}' is identified as a non-medical document.")

        return text
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous page title: {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
