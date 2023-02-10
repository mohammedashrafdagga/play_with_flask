from flask import Flask


# create app
app = Flask(__name__)

# create main route


@app.route('/')
def homepage():
    return 'Hello World'


# run app
if __name__ == '__main__':
    # now building
    app.run(port=3000, debug=True)
