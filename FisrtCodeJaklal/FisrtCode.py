from sklearn.linear_model import LinearRegression 
import numpy as jalalMolla
x=jalalMolla.array([[1],[2]])
y=jalalMolla.array([2,4])
model=LinearRegression()
model.fit(x,y)
new_input=jalalMolla.array([[3]])
prediction=model.predict(new_input)
print("Here I am Jalal Molla with Machine Learning: ",prediction[0])
