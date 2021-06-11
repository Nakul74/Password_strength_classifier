from flask import Flask
from pywebio.input import input,TEXT
from pywebio.output import put_text
from pywebio.platform.flask import webio_view
from feature_engineering import col_transform
import numpy as np
import argparse
from pywebio import start_server

from joblib import load
logreg = load('logreg.joblib') 
model = load('model.joblib')

app = Flask(__name__)


def predict():

    password = input("Enter the password：", type = TEXT)
    password = np.array([password])
    
    vect = model.transform(password)
    prediction = logreg.predict(vect)[0]
    
    if prediction == 0:
        strength = 'Weak'
    elif prediction == 1:
        strength = 'Medium'
    else :
        strength = 'Strong'
        
    put_text('Passowrd is : ',strength)
    

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)   
    
    
#app.run(host='localhost', port=80)