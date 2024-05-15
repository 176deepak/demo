from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    return "<h1>Webhook called</h1>"


if __name__ == "__main__":
    app.run()
