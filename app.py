from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio-details")
def portfolio_details():
    return render_template("portfolio-details.html")

@app.route("/service-details")
def service_details():
    return render_template("service-details.html")

if __name__ == "__main__":
    app.run(debug=True)