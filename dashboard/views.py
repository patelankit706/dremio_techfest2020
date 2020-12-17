from django.shortcuts import render

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
    print(input1,input2,input3,input4)
    #pred_score = sentimentAnalysisViews.sentiment_analyser(input_string)
    #print(pred_score)
    #pred_score=pred_score*100
    context={'input_string':input1}
    return render(request, 'fraud_detection.html',context)
