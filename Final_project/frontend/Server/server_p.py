from flask import Flask,request,jsonify
import pandas as pd
import numpy as np
import utility as util
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello! this is the SERVER1 page <h1>HELLO To OUR Page<h1>"

@app.route("/get_flight_names")
def getflightnames():
    response = jsonify({
        'flights':util.get_flight_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route("/get_source_names")
def getsourcenames():
    response = jsonify({
        'sources':util.get_source_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route("/get_destination_names")
def getdestinationnames():
    response = jsonify({
        'destinations':util.get_destination_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    print(util.get_destination_names())
    return response


@app.route('/predictFightPrice', methods=['GET', 'POST'])
def predict():
    # date_book = request.form["Book_Time"]
    date_dep = request.form["Dep_Time"]
    date_arr = request.form["Arrival_Time"]
    # date_diff = (pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M") - pd.to_datetime(date_book,format="%Y-%m-%dT%H:%M")).days
    # date_diff = np.int64(date_diff)
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
    Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
    Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
    weekday = ((pd.DatetimeIndex(Journey_day).dayofweek) // 5 == 1).astype(int)
    night_journey= 1 if Dep_hour>=21 else 0
    early_morning_journey= 1 if (Dep_hour>=4 & Dep_hour<=8) else 0
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    Total_stops = int(request.form["stops"])
    airline = request.form["airline"]
    additional_info=request.form["additionalinfo"]
    
    if (additional_info=='1 Long Layover'):
        additional_info=0
    elif(additional_info=='2 Long Layover'):
        additional_info=0
    elif(additional_info=='1 Short Layover'):
        additional_info=0
    elif(additional_info=='Change Airports'):
        additional_info=1
    elif(additional_info=='In-flight meal not included'):
        additional_info=2
    elif(additional_info=='No-check-In baggage included'):
        additional_info=4
    elif(additional_info=='Red-eye flight'):
        additional_info=6
    elif(additional_info=='No info'):
        additional_info=5

    
    
    if (airline=='Indigo'):
        airline=3
    elif(airline=='Jet Airways'):
        airline=4
    elif(airline=='SpiceJet'):
        airline==7
    elif(airline=='Air India'):
        airline=1
    elif(airline=='Multiple Carriers'):
        airline=5
    elif(airline=='Air Asia'):
        airline=0  
    elif(airline=='Vistara'):
        airline=9
    elif(airline=='GoAir'):
        airline=2
    elif(airline=='Multiple Carriers Premium Economy'):
        airline=6  
    elif(airline=='Trujet'):
        airline=8
    elif(airline=='Vistara Premium Economy'):
        airline=10
    elif(airline=='Trujet'):
        airline=8        
    # Source
    # Banglore = 0 (not in column)
    Source = request.form["Source"]
    if (Source == 'Delhi'):
        source_delhi = 1
        source_kolkata = 0
        source_mumbai = 0
        source_chennai = 0
        source_banglore=0

    elif (Source == 'Kolkata'):
        source_delhi = 0
        source_kolkata = 1
        source_mumbai = 0
        source_chennai = 0
        source_banglore=0
    elif (Source == 'Mumbai'):
        source_delhi = 0
        source_kolkata = 0
        source_mumbai = 1
        source_chennai = 0
        source_banglore=0
    elif (Source == 'Chennai'):
        source_delhi = 0
        source_kolkata = 0
        source_mumbai = 0
        source_chennai = 1
        source_banglore=0

    elif (Source == 'Banglore'):
        source_delhi = 0
        source_kolkata = 0
        source_mumbai = 0
        source_chennai = 0
        source_banglore=1

    else:
        source_delhi = 0
        source_kolkata = 0
        source_mumbai = 0
        source_chennai = 0
        source_banglore=0

    print(source_delhi,
        source_kolkata,
        source_mumbai,
        source_chennai)

    # Destination
    # Banglore = 0 (not in column)
    Source = request.form["Destination"]
    if (Source == 'Cochin'):
        destination_cochin = 1
        destination_delhi = 0
        destination_new_delhi = 0
        destination_hyderabad = 0
        destination_kolkata = 0
        destination_banglore=0

    elif (Source == 'Delhi'):
        destination_cochin = 0
        destination_delhi = 1
        destination_new_delhi = 0
        destination_hyderabad = 0
        destination_kolkata = 0
        destination_banglore=0
    elif (Source == 'New_Delhi'):
        destination_cochin = 0
        destination_delhi = 0
        destination_new_delhi = 1
        destination_hyderabad = 0
        destination_kolkata = 0
        destination_banglore=0
    elif (Source == 'Hyderabad'):
        destination_cochin = 0
        destination_delhi = 0
        destination_new_delhi = 0
        destination_hyderabad = 1
        destination_kolkata = 0
        destination_banglore=0
    elif (Source == 'Kolkata'):
        destination_cochin = 0
        destination_delhi = 0
        destination_new_delhi = 0
        destination_hyderabad = 0
        destination_kolkata = 1
        destination_banglore=0

    elif (Source == 'Banglore'):
        destination_cochin = 0
        destination_delhi = 0
        destination_new_delhi = 0
        destination_hyderabad = 0
        destination_kolkata = 0
        destination_banglore=1
    else:
        destination_cochin = 0
        destination_delhi = 0
        destination_new_delhi = 0
        destination_hyderabad = 0
        destination_kolkata = 0
        destination_banglore=0


    response = jsonify({
        'estimated_price': util.get_estimated_price(
            airline,
            Total_stops,
            additional_info,
            Journey_day,
            Journey_month,
            weekday,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            night_journey,
            early_morning_journey,
            dur_hour,
            dur_min,
            source_banglore,
            source_chennai,
            source_delhi,
            source_kolkata,
            source_mumbai,
            destination_banglore,
            destination_cochin,
            destination_delhi,
            destination_hyderabad,
            destination_kolkata,
            destination_new_delhi)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response





if __name__=="__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True)