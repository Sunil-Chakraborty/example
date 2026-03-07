from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    data = {
        "title": "Sample Report",
        "items": ["Item A", "Item B", "Item C"]
    }
    return render_template("report.html", data=data)

if __name__ == "__main__":
    app.run()
