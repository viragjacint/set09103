from flask import Flask, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
  return "The default, 'root' route"

@app.route("/static/")
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

