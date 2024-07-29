import json
import pickle
import numpy as np

# make global vars
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower()) # this is to locate the column index of the location. not using np bcs __data.columns is a list, not an array.
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns)) # make an initial zeros array so the encoding works properly. all locs will be 0 except the selected loc
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1 # for the selected loc, we set the encoded loc as 1

    return round(__model.predict([x])[0],2) # we get 2d array back after the pred, but our array has only 1 element. so, access the estimated price which is in the 0 index.


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading artifacts start")
    global __data_columns
    global __locations

    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    with open("server/artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts done")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("anekal", 1000, 3, 3))
    print(get_estimated_price("anekal", 1000, 2, 2))
    print(get_estimated_price("bisuvanahalli", 800, 2, 2))
    print(get_estimated_price("bisuvanahalli", 800, 1, 1))
    