from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')  #just a / means on the base URL
def endpoint_1(): #this method can be named anything
    return jsonify(message='first end point')

if __name__ == '__main__':
    app.run()