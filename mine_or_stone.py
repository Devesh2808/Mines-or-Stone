# -*- coding: utf-8 -*-
"""Mine or Stone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sdwApPjn8UciJk6B0Fg6Qz4gDtAGK-lc

Importing The Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection And Data Processing"""

sonar_data=pd.read_csv('/content/sonar data.csv',header=None)
sonar_data.head()

#number of rows and column
sonar_data.shape

sonar_data.describe() #describe ---> Statistical measures of  the data

#to check the no of rocks(R) and mines(M) in the dataset
sonar_data[60].value_counts()  #[60]---> col no ,where R and M are stored

"""To get accurate answer there should be almost equal no of both the cases i.e., R and M """

sonar_data.groupby(60).mean()

#separating the data and labels(R and M) by droping from orig data and storing in new var, as  R or M is our answer ,we will train with that
X = sonar_data.drop(columns=60,axis =1)
Y = sonar_data[60]

print(X,Y)

"""Split into Training and Test data"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)
#X_train--> data for training,Y_train--->respective label for train(R,M)
#X_test---> data for test,Y_test--->respective label for train(R,M)
#stratify=Y ----> Split on the basis of Y(R,M) -->equal no of R,M in Test and Train data for better accuracy
#test_size=0.1-->10% test data from total data

print(X.shape,X_train.shape,X_test.shape)

"""Model Training"""

#Logistic Regression
#model =LogisticRegression()

#KNN
#from sklearn.neighbors import KNeighborsClassifier
#model=KNeighborsClassifier()

#GaussianNB
#from sklearn.naive_bayes import GaussianNB
#model=GaussianNB()

#RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()

model.fit(X_train,Y_train)

"""Model Evaluation"""

#accuracy  on training data
X_train_prediction = model.predict(X_train) #predict the result(R or M)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train) #compre with original answer 
#X_train_prediction will be compared with the answer i.e, Y_train
#accuracy(value for comparison , comparison with)

print('Accuracy for training data : ', training_data_accuracy)

#accuracy  on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy for test data : ', test_data_accuracy)

"""Creation of Predictive System for R(Rock) and M(Mine)"""

#take some input data for predicion from our trained model
input_data = (0.0274,0.0242,0.0621,0.0560,0.1129,0.0973,0.1823,0.1745,0.1440,0.1808,0.2366,0.0906,0.1749,0.4012,0.5187,0.7312,0.9062,0.9260,0.7434,0.4463,0.5103,0.6952,0.7755,0.8364,0.7283,0.6399,0.5759,0.4146,0.3495,0.4437,0.2665,0.2024,0.1942,0.0765,0.3725,0.5843,0.4827,0.2347,0.0999,0.3244,0.3990,0.2975,0.1684,0.1761,0.1683,0.0729,0.1190,0.1297,0.0748,0.0067,0.0255,0.0113,0.0108,0.0085,0.0047,0.0074,0.0104,0.0161,0.0220,0.0173)
input_data_as_numpy_array = np.asarray(input_data) #converts the data as array

#reshape the np array as we are predicting for one instance(input)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) #for single instances 
prediction =model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]=='R'):  
 print('The object is a Rock')
else:
 print('The obejct is a Mine')

"""KNN model has better accuracy than Logistic Regression"""