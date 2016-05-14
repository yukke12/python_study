from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/aa")
def hello2():
	return 'hello2!!'

if __name__ == "__main__":
    app.run()

