import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def predictmark(hrs):
    hrs=int(hrs)
    hr=np.array(hrs).reshape(-1,1)
    data=pd.read_csv(r"C:\Users\ravik\OneDrive\Desktop\ml\miniprojects\models\marks.csv")
    print("readed")
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    X=data['time_study'].values
    Y=data['Marks'].values

    X=X.reshape(-1,1)
    Y=Y.reshape(-1,1)
    train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.2,random_state=42)
    model=LinearRegression()
    model.fit(train_x,train_y)
    final=model.predict(hr)
    return final