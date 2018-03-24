from sklearn import linear_model
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data=pd.read_excel('Book1.xlsx')
a=data['Day']
x=data['Order']
y=data['warehouse']
z=data['produced']
infea1=pd.DataFrame(x)#input features
infea2=pd.DataFrame(y)#input features
tar=pd.DataFrame(z)#prediction
X=infea1
Y=infea2
Z=tar
lm =linear_model.LinearRegression()
model =lm.fit(X,Z)
predictions = lm.predict(Z)
print(lm.score(X,Z))
plt.plot(a,Z)
plt.show()
