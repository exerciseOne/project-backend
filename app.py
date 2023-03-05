from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return render_template('hello.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello_form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('hello.html', name=name)

    return render_template('helloWorldForm.html')
