import wikipedia

def get_medical_title(number):
    wikipedia.set_lang("en")

    # Get category members for the "Medical" category
    medical_category = wikipedia.page("Category:Health")
    medical_titles = medical_category.links
    return [title for title in medical_titles[:number] if "Category:" not in title]

def get_non_medical_title(number):
    wikipedia.set_lang("en")

    medical_category = wikipedia.page("Category:Game")
    medical_titles = medical_category.links
    return [title for title in medical_titles[:number] if "Category:" not in title]

def get_wikipedia_text(page_title):
    try:
        page = wikipedia.page(page_title)
        text = page.content
        return text
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous page title")
    except wikipedia.exceptions.PageError as e:
        print("Page not found")
    except Exception as e:
        print("An error occurred")

def get_content(number:10,medical:True):
    contents=[]
    titles=None
    if medical:
        titles=get_medical_title(number)
    else:
        titles=get_non_medical_title(number)
    for title in titles:
             content=get_wikipedia_text(title)
             if content!=None:
                 contents.append(content)
    return contents

