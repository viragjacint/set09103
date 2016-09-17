from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
  return "The default, 'root' route"

app.route("/force404/")
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

