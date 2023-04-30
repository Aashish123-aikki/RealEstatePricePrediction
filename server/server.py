from flask import Flask,request,jsonify
import util
app=Flask(__name__)
@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_price',methods=['POST'])
def predict_price():
    total_sqft=float(request.form['total_sqft'])
    bhk=int(request.form['bhk'])
    location=request.form['location']

    
    response=jsonify({
        'estimatedprice':util.get_estimated_value(location,total_sqft,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
if __name__=='__main__':
    print("Sucesssfully started")
    util.load_artifacts()
    app.run()