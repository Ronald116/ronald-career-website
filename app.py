from flask import Flask, render_template, jsonify

flask_app = Flask(__name__, template_folder='templates')

JOBS = [
    {"id": 1, "title": "Front-End Deveoloper", "location": "Accra", "salary": "GHS 3000.00"},
    {"id": 2, "title": "Data Analyst", "location": "Accra", "salary": "GHS 4000.00"},
    {"id": 3, "title": "Back-End Deveoloper", "location": "Tema", "salary": "GHS 3500.00"},
    {"id": 4, "title": "Data Scientist", "location": "Legon", "salary": "GHS 5000.00"},
    {"id": 5, "title": "Fullstack Deveoloper", "location": "Accra", "salary": "GHS 4500.00"}
]

@flask_app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

@flask_app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    flask_app.run(host= "0.0.0.0", debug=True)
    