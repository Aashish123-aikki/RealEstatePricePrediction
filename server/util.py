import json
import pickle
import numpy as np
__location=None
__model=None
__data_col=None

def get_estimated_value(location,sqft,bhk):
    try:
        loc_index=__data_col.index(location.lower())
    except:
        loc_index =-1
    
    x=np.zeros(len(__data_col))
    x[0]=sqft
    x[1]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __location

def load_artifacts():
    print("loading artifacts")
    global __data_col
    global __location
    global __model
    with open('server/artifacts/columns.json','r') as f:
        __data_col=json.load(f)['datacolmn']
        __location=__data_col[2:]
    with open('server/artifacts/banglurumodel.pickle','rb') as f:
        __model=pickle.load(f)
    print('artifacts load sucessfull')
if __name__=='__main__':
    load_artifacts()
    print(get_location_names())
    print(get_estimated_value('kalhalli',1000,2))
