from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
  #test for user login
  #if failed redirect to login
  return redirect(url_for('login'))

@app.route('/login/')
def login():
  return "Username & Password"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

