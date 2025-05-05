import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
csv = pd.read_csv("sgpa_prediction_dataset.csv")
X=csv[["Study Hours/Day","Previous SGPA","Attendance (%)","Assignment Submission Rate (%)","Sleep Hours/Day"]]
y=csv[["SGPA (Target)"]]
#splitting the data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4)
#building the model
reg=linear_model.LinearRegression()
model=reg.fit(X_train,y_train)
#predicting the model
predictions=model.predict(X_test)
listformat=predictions.tolist()
print("Prediction is: ",listformat)
from sklearn import metrics
#accuracy
r2=metrics.r2_score(y_test,predictions)
print(f"R^2 value is: {r2:.2f}")
fig,ax = plt.subplots(figsize=(9, 7))
x=range(len(y_test))
ax.plot(x,y_test,color="r",label="True Values")
ax.plot(x,predictions,color="b",label="Predictions")
ax.set_xlabel("Index")
ax.set_ylabel("SGPA")
ax.set_title("True Values vs Predictions")
ax.legend()
plt.show()


