from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>You are going to be a good devops!</h1>"


@app.route("/second")
def second():
    return "<h1>This is my second page</h1>"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page .. Francis</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'<h1>Id of this page is {id}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
