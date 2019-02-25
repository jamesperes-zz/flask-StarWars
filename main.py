from flask import Flask, render_template
from details import get_person

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail/<int:id>')
def detail(id):
    films_not_showed = get_person(id)
    return render_template('details.html', films_not_showed=films_not_showed)

if __name__ == '__main__':
    app.run(host='0.0.0.0')