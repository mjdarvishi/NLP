from flask import Flask, render_template,request

from wiki_data_source import get_wikipedia_text
from bag_of_word_model import check,accuracy,classification_rep
from data_repository import get_non_medical_title,get_medical_title
app = Flask(__name__)


@app.route('/')
def home():
    data=get_medical_title()
    data1=get_non_medical_title()
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
    return render_template('detail_page.html',data=data,title=name)

@app.route('/statistics')
def statistics():
    return render_template('statistics.html',accur=accuracy,report=classification_rep)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
