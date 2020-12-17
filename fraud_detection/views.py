from django.shortcuts import render
from django.conf import settings as conf
import pickle
import os

# Create your views here.
def load_model():
    model_path=os.path.join(conf.MODELS_DIR, './xgb_model.pkl')
    pred_model=pickle.load(open(model_path, "rb"))
    return pred_model

pred_model=load_model()
print('load success')

def make_pred(user_input):
    prediction = pred_model.predict(user_input)
    return prediction
