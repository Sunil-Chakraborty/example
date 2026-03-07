from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return "<h2>Sample Report Page</h2><p>This is your reporting system.</p>"

if __name__ == "__main__":
    app.run()
