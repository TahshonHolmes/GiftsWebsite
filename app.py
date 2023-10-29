from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def submit_answer():
    answer = request.form.get('answer')
    if answer.lower() == 'grimm':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('grimm'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/grimm')
def grimm():
    return render_template('grimm.html')

if __name__ == '__main__':
    app.run(debug=True)
