import wikipedia

def get_medical_title(number):
    # Set the language to English
    wikipedia.set_lang("en")

    # Get category members for the "Medical" category
    medical_category = wikipedia.page("Category:Medical")
    medical_titles = medical_category.links
    # Filter out non-medical titles
    return [title for title in medical_titles[:number] if "Category:" not in title]

def get_non_medical_title(number):
    # Set the language to English
    wikipedia.set_lang("en")

    # Get category members for the "Medical" category
    medical_category = wikipedia.page("Category:Game")
    medical_titles = medical_category.links
    # Filter out non-medical titles
    return [title for title in medical_titles[:number] if "Category:" not in title]

def get_wikipedia_text(page_title):
    try:
        page = wikipedia.page(page_title)
        text = page.content
        return text
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous page title: {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_content(number:10,medical:True):
    if medical:
        return [get_wikipedia_text(title) for title in get_medical_title(number)]
    else:
        return [get_wikipedia_text(title) for title in get_non_medical_title(number)]

