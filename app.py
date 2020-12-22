from flask import Flask, render_template, request
from api import Api

app = Flask(__name__)
app.secret_key = "Hello"
api = Api()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/dev", methods = ["GET", "POST"])
def dev():
	if request.method == "POST":
		raw_code = str(request.form["code"])
		code = ""
		for line in raw_code.splitlines():
			code += eval(line)
		return code
	else:
		return render_template("dev.html")

if __name__ == "__main__":
	app.run(debug = True)