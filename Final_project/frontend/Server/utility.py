import json
import pickle
import numpy as np

__model = None
__location = None
__data_columns = None
__flight = None
__source = None
__destination = None


def get_estimated_price(airline, total_stops, additional_info, day_of_travel, month_of_travel, weekday, depart_hour,
                        depart_minute, arrival_hour, arrival_minute, night_journey, early_morning_journey, travel_hour, 
                        travel_minute, source_banglore, source_chennai, source_delhi, source_kolkata, source_mumbai, 
                        destination_banglore, destination_cochin, destination_delhi, destination_hyderabad, destination_kolkata, 
                        destination_new_delhi):
    load_saved_artifacts()
    print("PREDICTION")
    prediction = __model.predict([[airline, total_stops, additional_info, day_of_travel, month_of_travel, weekday, depart_hour,
                        depart_minute, arrival_hour, arrival_minute, night_journey, early_morning_journey, travel_hour, 
                        travel_minute, source_banglore, source_chennai, source_delhi, source_kolkata, source_mumbai, 
                        destination_banglore, destination_cochin, destination_delhi, destination_hyderabad, destination_kolkata, 
                        destination_new_delhi
    ]])

    output = round(prediction[0], 2)
    print(output)
    return output


def get_location_names():
    load_saved_artifacts()
    return __location

def get_flight_names():
    load_saved_artifacts()
    b=[]
    for i in __flight:
        b+=i.split("_")
    for i in b:
        if "airline" in i:
            b.remove("airline")
    b = [i.title() for i in b]
    return b

def get_source_names():
    load_saved_artifacts()
    b=[]
    for i in __source:
        b+=i.split("_")
    for i in b:
        if "source" in i:
            b.remove("source")
    b = [i.title() for i in b]
    return b

def get_destination_names():
    load_saved_artifacts()
    b=[]
    for i in __destination:
        b+=i.split("_")
    for i in b:
        if "destination" in i:
            b.remove("destination")
    b = [i.title() for i in b]
    return b



def load_saved_artifacts():
    global __model
    global __location
    global __data_columns
    global __flight
    global __source
    global __destination

    with open("C:\Workspace\Sem 4\PRML\Bonus Project\Final_project\columns_diff.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[0:]
        __flight = __data_columns[0]
        __source = __data_columns[14:19]
        __destination = __data_columns[19:]

    with open("C:\Workspace\Sem 4\PRML\Bonus Project\Final_project\model.pkl", 'rb') as f:
        print("Load FILE")
        __model = pickle.load(f)


if __name__ == '__main__':
    print(get_location_names())
    print(get_flight_names())
    print(get_source_names())
    print(get_destination_names())
