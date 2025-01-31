import pandas as pd 
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann
import pickle
import os

model = pickle.load(open('C:/Users/Notebook/repos/DS-Producao/model_rossmann.pkl','rb'))

app = Flask(__name__)

# initialize API
@app.route('/rossmann/predict', methods = ['POST'])
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json,dict): #unique example
            test_raw = pd.DataFrame(test_json, index[0])
            
        else: # multiple example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Rossamann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
        
    else:
        Response('{}', status = 200, mimetype = 'application/json')
        
if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run('192.168.18.4',port=port)