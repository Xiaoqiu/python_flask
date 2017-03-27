from flask import Flask
from flask import jsonify
import test
import main.nltk.nltk_keywords as nltkm

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TESTING=True,
    TEMPLATES_AUTO_RELOAD=True
)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')
def hello_world():
    return 'Hello World hhhh!'

@app.route('/h')
def h():
    return 'Hello World wwwww!'

@app.route('/say')
def say():
    return test.say()

@app.route('/test')
def test():
     return nltkm.test()

@app.route('/keywords')
def keywords():
    return jsonify(nltkm.lexical_diversity('hello you hello me'))

@app.route('/count_words')
def count_words():
    return nltkm.count_words()

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()
