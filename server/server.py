from flask import Flask, request, jsonify
# flask is a module that allows user to write pyhton service which can serve HTTP request
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    # returning a response which contains all the locations:
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # whenever we want to makw http call from html app, we'll get all the inputs in the request form. see below:
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])


    # returning a response which contains estimated price:
    response = jsonify({
        'estimated_price':util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    

if __name__=="__main__":
    util.load_saved_artifacts() # if I dont add this here, the postman will give results of 'locations': [null]
    print("starting python flask server")
    app.run()


## 1. run this server.py in terminal -> pyhton server/server.py
## 2. copy the http in the postman to check