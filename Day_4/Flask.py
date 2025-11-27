from flask import Flask, render_template, request

app = Flask(__name__, template_folder='views')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hi')
@app.route('/hi/<name>')
def hi_get(name='Lukasz'):
    return render_template('hi.html', t_name=name)

@app.route('/hi_for_ai', methods=['POST'])
def hi_post():
    name = request.form['first_name']
    age = request.form['age']

    return render_template('hi.html', t_name=name, t_age=age)

app.run(debug=True)


