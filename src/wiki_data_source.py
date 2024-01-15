import wikipedia

def get_geographic_title(number):
    wikipedia.set_lang("en")

    # Get category members for the "geographic" category
    geographic_category = wikipedia.page("Category:continent")
    geographic_titles = geographic_category.links
    return [title for title in geographic_titles[:number] if "Category:" not in title]

def get_non_geographic_title(number):
    wikipedia.set_lang("en")

    geographic_category = wikipedia.page("Category:Game")
    geographic_titles = geographic_category.links
    return [title for title in geographic_titles[:number] if "Category:" not in title]

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

def get_content(number:10,geographic:True):
    contents=[]
    titles=None
    if geographic:
        titles=get_geographic_title(number)
    else:
        titles=get_non_geographic_title(number)
    for title in titles:
             content=get_wikipedia_text(title)
             if content!=None:
                 contents.append(content)
    return contents

