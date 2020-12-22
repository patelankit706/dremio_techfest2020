from django.shortcuts import render
from django.conf import settings as conf
import pickle
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
#import pyodbc



# Create your views here.
def model_retrain():
    host = '74.91.21.100'
    port = 31010
    uid = 'letaptikna'
    pwd = '9039396188as'
    driver = "Dremio Connector"
    cnxn=pyodbc.connect("Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(driver,host,port,uid,pwd),autocommit=True)
    sql = '''SELECT * FROM "@letaptikna".clean_ny'''
    df = pd.read_sql(sql,cnxn)
    df = df.rename(columns={'oldbalanceOrg':'oldBalanceOrig', 'newbalanceOrig':'newBalanceOrig', \
                            'oldbalanceDest':'oldBalanceDest', 'newbalanceDest':'newBalanceDest'})
    df['errorBalanceOrig'] = df.newBalanceOrig + df.amount - df.oldBalanceOrig
    df['errorBalanceDest'] = df.oldBalanceDest + df.amount - df.newBalanceDest
    enc = LabelEncoder()
    df['type'] = enc.fit_transform(df['type'])
    Y = df.isFraud
    X = df.drop(['isFraud'],axis=1)
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X.values,Y.values,test_size=0.2, random_state = 1)
    # scale_pos_weight should be ratio of negative classes to positive classes
    weights = (Y == 0).sum() / (Y == 1).sum()
    clf = XGBClassifier(max_depth = 3, scale_pos_weight = weights, n_jobs = 4)
    clf.fit(Xtrain,Ytrain)
    pickle.dump(clf, open(os.path.join(conf.MODELS_DIR, './xgb_model.pkl'), "wb"))
    print('Retraining Successful')




def load_model():
    model_path=os.path.join(conf.MODELS_DIR, './xgb_model.pkl')
    pred_model=pickle.load(open(model_path, "rb"))
    return pred_model

pred_model=load_model()
print('load success')

def make_pred(user_input):
    prediction = pred_model.predict(user_input)
    return prediction
