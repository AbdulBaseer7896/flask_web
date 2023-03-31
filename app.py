from flask import Flask, render_template, jsonify, request
from con_database import load_jobs_from_db


# JOBS = []

app = Flask(__name__)

@app.route("/")
def hello_baseer():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
