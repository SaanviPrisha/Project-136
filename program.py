from flask import Flask, request
from flask.json import jsonify

from data import data

app = Flask(__name__)

@app.route("/")
def simple():
    return("You are on the simple version of the API. To see any data, please specify in the URL based on the routing given in this file.")

@app.route('/all-stars')
def all_stars_data():
    return jsonify({
        'data': data,
        'message': "success"
    }), 200

@app.route('/specific_star')
def specific_star():
    name = request.args.get('name')
    star_data = next(item for item in data if item[name] == name)
    return jsonify({
        'data': star_data,
        'message': 'success'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
else:
    print("The code is not working properly. Please check for any errors.")