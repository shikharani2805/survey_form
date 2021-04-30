
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/survey_db"

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        form_data = mongo.db.survey_data
        existing_user = form_data.find_one({'email': request.form['email']})
        if existing_user is None:
            _name = request.form['name']
            _email = request.form['email']
            _age = request.form['age']
            _role = request.form['role']
            _likely = request.form['likely']
            _fcc = request.form['fcc']
            _work = request.form.getlist('work')

            form_data.insert({'name': _name, 'email': _email, 'age': _age, 'role': _role, 'likely': _likely, 'fcc': _fcc, 'work': _work})
            return 'Thank for response'
        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
