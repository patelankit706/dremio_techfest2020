from django.shortcuts import render
import pickle

# Create your views here.
def load_model():
    model_path=os.path.join(conf.MODEL_DIR, './xgb_reg.pkl')
    pred_model=pickle.load(open(model_path, "rb"))
    return pred_model

pred_model=load_model()
print('load success')

def make_pred(user_input):
    prediction = pred_model.predict(user_input)[1]
        return prediction
