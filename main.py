from datetime import datetime 
import pull_stock  as pt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
import joblib as j
import json



def main(df):
    print(df.info())
    df["Volume"]= df['Volume'].astype('float')
    df.drop(columns=["Volume"],inplace=True)
    print(df.describe())
    s = StandardScaler()
    feature = ["Close", "High", "Low", "Open"]
    df_scaled_array = s.fit_transform(df[feature])
    X = pd.DataFrame(df_scaled_array, columns=feature)
    y = df["Target"]
    X_Train,X_Test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 1)
    model = SVC(kernel="linear")
    model.fit(X_Train,y_train)
    j.dump(model,'model.pkl')
    y_pred = model.predict(X_Test)
    acc = round(accuracy_score(y_test,y_pred),2)
    print(f"Accuracy:{acc}")
    
    # Save metrics for DVC tracking
    with open('metrics.json', 'w') as f:
        json.dump({"accuracy": acc}, f)
    
if __name__ == '__main__':
    company_name = "GOOGL" 
    start_date =  datetime(2004,8,19).date()
    end_date = datetime.now().date()
    current_stock_history = pt.pull_stock_data(company_name,start_date,end_date)
    df= pt.PreProcessing(current_stock_history)
    main(df)