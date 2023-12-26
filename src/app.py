from flask import Flask, render_template,request

from wiki_data_source import get_wikipedia_text
from classifier_core import check_with_navie,check_with_logistice,naive_bayes_accuracy,logistic_regression_accuracy,logistic_regression_report,naive_bayes_report
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
    result=check_with_navie(user_input)
    if result==None:
        return render_template('result.html', user_input='Your title has no wiki page')
    return render_template('result.html', user_input=result)

@app.route('/logistic', methods=['POST'])
def logistic():
    user_input = request.form.get('data')
    result=check_with_logistice(user_input)
    if result==None:
        return render_template('result.html', user_input='Your title has no wiki page')
    return render_template('result.html', user_input=result)


@app.route('/detail/<name>')
def detail_page(name):
    data=get_wikipedia_text(name)
    return render_template('detail_page.html',data=data,title=name)

@app.route('/statistics')
def statistics():
    return render_template('statistics.html',accur=naive_bayes_accuracy,report=naive_bayes_report)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/statistics-logestic')

def statistics_logestic():
    return render_template('statistics.html',accur=logistic_regression_accuracy,report=logistic_regression_report)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
