from flask import Flask, render_template, url_for

app = Flask(__name__,template_folder='./template')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("login")
def login():
    return render_template('login.html')

@app.route('education')
def education():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug = True)
