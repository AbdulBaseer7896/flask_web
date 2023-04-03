from flask import Flask, render_template, jsonify, request
from con_database import load_jobs_from_db , get_password

 
# JOBS = []

app = Flask(__name__)

@app.route("/")
def hello_baseer():
  return render_template('sign_in.html')

@app.route("/sign" , methods = ["POST", "GET"])
def sign():
  if request.method == "POST":
    emails = request.form['email']
    passowards = int(request.form['passoward'])
    print(f"email = {emails} and pasww = {passowards}")
  return render_template('index.html')

@app.route('/home' , methods = ["POST", "GET"])
def home():
  if request.method == "POST":
    emails = request.form['email']
    passowards = int(request.form['passoward'])
    print(f"email = {emails} and pasww = {passowards}")
  
  key = [((emails), passowards)]
  key_db = get_password()
  if key == key_db:
    jobs = load_jobs_from_db()
    return render_template('home.html' , jobs = jobs)
  return hello_baseer()
    
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
