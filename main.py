from flask import Flask
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Функция получения текущего времени
def get_current_time():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

@app.route('/time')
def home():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return f"""
    <h1>Текущие дата и время</h1>
    <p>{current_time}</p>
    """

@app.route('/')
def index():
    return render_template('index.html', current_time=get_current_time())

@app.route('/blog/')
def blog():
    return render_template('blog.html', current_time=get_current_time())

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', current_time=get_current_time())


if __name__ == '__main__':
    app.run(debug=True)