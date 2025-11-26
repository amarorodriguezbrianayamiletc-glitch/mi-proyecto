from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biografia')
def biografia():
    return render_template('biografia.html')

@app.route('/discografia')
def discografia():
    return render_template('discografia.html')

@app.route('/visuales')
def visuales():
    return render_template('visuales.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

if __name__ == '__main__':
    app.run(debug=True)