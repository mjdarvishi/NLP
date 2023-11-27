from flask import Flask, render_template,request

# print the updated sys.path

from wiki_data_source import get_medical_title,get_non_medical_title,get_wikipedia_text
from bag_of_word_model import check
app = Flask(__name__)


@app.route('/')
def home():
    data=get_medical_title(number=50)
    data1=get_non_medical_title(number=50)
    return render_template('home.html',data=[data,data1])

@app.route('/', methods=['POST'])
def index():
    user_input = request.form.get('data')
    result=check(user_input)
    if result==None:
        return render_template('result.html', user_input='Your title has no wiki page')
    return render_template('result.html', user_input=result)

@app.route('/detail/<name>')
def detail_page(name):
    data=get_wikipedia_text(name)
    # Render the detail page with the parameters
    return render_template('detail_page.html',data=data,title=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
