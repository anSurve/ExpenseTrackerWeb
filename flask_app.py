from flask import Flask, render_template
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/apps')
def apps():
    return render_template('apps.html')


@app.route('/expense_tracker')
def expense_tracker():
    return render_template('expense_tracker.html')


if __name__ == '__main__':
    app.run()