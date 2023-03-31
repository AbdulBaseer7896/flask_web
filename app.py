from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Pakistan Islamabad',
    'salary': 'Rs 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Pakistan Lahore',
    'salary': 'Rs 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Enginerr',
    'location': 'usa',
    # 'salary': 'Rs 12,00,000'
  },
  {
    'id': 4,
    'title': 'Back-end Enginerr',
    'location': 'Remore',
    'salary': 'Rs &120,00'
  }
]


@app.route("/")
def hello_world():
  print("this is web page")
  return render_template("home.html", name="Qazi Abdul", jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
