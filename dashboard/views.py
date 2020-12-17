from django.shortcuts import render
from fraud_detection import views as fraud_detectionViews
import numpy as np
# Create your views here.
def index(request):
    return render(request, 'tableau.html')

def tableau(request):
    return render(request, 'tableau.html')

def fraud_detection(request):
    print('ML Model')
    return render(request, 'fraud_detection.html')

def fraud_detection_pred(request):
    print('Entered ML model')
    input1 = request.POST.get('InputText1')
    input2 = request.POST.get('InputText2')
    input3 = request.POST.get('InputText3')
    input4 = request.POST.get('InputText4')
    input5 = request.POST.get('InputText5')
    input6 = request.POST.get('InputText6')
    input7 = request.POST.get('InputText7')
    input8 = request.POST.get('InputText8')
    input9 = request.POST.get('InputText9')
    user_input=np.array([float(input1),float(input2),float(input3),float(input4),float(input5),float(input6),float(input7),float(input8),float(input9)]).reshape(1, -1)
    print(user_input,type(user_input),user_input.shape)
    prediction=fraud_detectionViews.make_pred(user_input)
    print(prediction,len(prediction))
    if prediction[0]==0:
        prediction_text='Safe'
    elif prediction[0]==0:
        prediction_text='Fradulent'  
    flag=len(prediction)    
    context={'flag':flag,'prediction_text':prediction_text}
    return render(request, 'fraud_detection.html',context)
