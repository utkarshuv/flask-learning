from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')  #just a / means on the base URL
@app.route('/home')
def home_page(): #this method can be named anything
    # return jsonify(message='first end point')
    return "<h1>Home Page</h1>"

@app.route('/about')
def about_page():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
