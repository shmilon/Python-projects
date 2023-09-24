import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model,model_selection
import os.path # using for receiving the directory path 
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import pathlib
import pickle # pickle using to save the trained data


# 'pickle.format_version' returns the version of pickle. 
# concatenating the pickle version with model name
# like price_model_4.0.pickle

# making a string so that we can save file name as it is
# price_model_4.0.pickle
dataset = 'price_model_'+pickle.format_version+'.pickle' 



if os.path.exists(dataset):
    
    print('\n*******************************')
    print('Loading Trained File')

    # if dataset/ trained model file exist then it will load to use
    model = pickle.load(open(dataset,"rb"))

else:
    print('\nCreating and training a new model')


    dir = os.path.dirname(__file__) # getting the directory path where the main.py file is
    data = pd.read_csv(dir+'/PotatoPrice.csv') # reading the dataset csv file

    X = data[['potato_kg']] #column 1 in csv file
    Y = data[['price']] # column 2 in csv file

    print('Model Training Started')
    print('*******************************')

    # training the model
    X_train,X_test, Y_train,Y_test = train_test_split(X,Y,test_size =0.3)
    model = tf.keras.Sequential([tf.keras.layers.Dense(1,input_shape=[1],activation='linear')])
    model.compile(optimizer ='sgd',loss='mean_squared_error',metrics=['accuracy'])
    model.fit(X_train,Y_train, epochs=500)

         
    print('*******************************')
    print("Model Trained Successfully")

    #saving the trained model as file
    with open(dataset,"wb") as file:
        pickle.dump(model, file)
    print("Saved Model Trained Successfully")


    # loading the saved trained model to use
    model = pickle.load(open(dataset,"rb"))



#predictions = model.predict(X)
#model.predict(X_test)
#print(model.predict([[10]]))

# prediction tool returns prediction result in array like [[120]]
# we can show this type of result to our user
#so here normalize_predict method will remove the [[]] brackets
# finally it will return 120 as string

def normalize_predict(kg):
    res = model.predict([[kg]]) # using model.prediction([[kg]]) we will get the predicted result like [[120]]
    res = str(res) 
    res = res.replace(']]','') #removing brackets
    res = res.replace('[[','') #removing brackets
    return res  #return the result without brackets


#result = normalize_predict(10)

# while loop for checking the result manually
# i=1
# while i==i:
#     print("how much kg?: ")
#     k= input()
#     print(normalize_predict(float(k)))