from django.shortcuts import render,HttpResponse
import pickle
import numpy as np
import pandas as pd
from .models import MedicalPremium
from datetime import datetime
# Create your views here.
def MedicalCost(response):
    return render(response,'costPrediction/medicalpremium.html')

def YesOrNo(query):
    if int(query)==1:
        return 'YES'
    return 'NO'

def result(response):
    rfr = pickle.load(open("RandomForestRegressor.pkl","rb"))
    if response.method == 'POST' and 'Predict' in response.POST:
        temp={}
        temp['Age'] = response.POST.get('Age')
        temp['Diabetes'] = response.POST.get('Diabetes')
        temp['BloodPressureProblems'] = response.POST.get('BloodPressureProblems')
        temp['AnyTransplants'] = response.POST.get('AnyTransplants')
        temp['AnyChronicDiseases'] = response.POST.get('AnyChronicDiseases')
        temp['Height'] = response.POST.get('Height')
        temp['Weight'] = response.POST.get('Weight')
        temp['KnownAllergies'] = response.POST.get('KnownAllergies')
        temp['HistoryOfCancerInFamily'] = response.POST.get('HistoryOfCancerInFamily')
        temp['NumberOfMajorSurgeries'] = response.POST.get('NumberOfMajorSurgeries')

        testdata = pd.DataFrame({'x':temp}).transpose()
        predictedData = rfr.predict(testdata)

    context={
        'name' : response.POST.get('Name'),
        'age': temp['Age'],
        'diabetes':YesOrNo(temp['Diabetes']),
        'bloodPressureProblems':YesOrNo(temp['BloodPressureProblems']),
        'transplants':YesOrNo(temp['AnyTransplants']),
        'chronicDiseases':YesOrNo(temp['AnyChronicDiseases']),
        'height': temp['Height'],
        'weight': temp['Weight'],
        'allergies':YesOrNo(temp['KnownAllergies']),
        'cancerInFamily':YesOrNo(temp['HistoryOfCancerInFamily']),
        'surgeries': temp['NumberOfMajorSurgeries'],
        'premium': round(predictedData[0])
        }
    return render(response,'costPrediction/result.html',context)

# def View_Database(response):
#     if response.method == 'POST' and 'saveToDB' in response.POST:
#         new_data = MedicalPremium(
#             Name='name',
#             Age='age'
#             Diabetes='diabetes'
#             BloodPressureProblems='bloodPressureProblems'
#             Transplants='transplants'
#             ChronicDiseases='chronicDiseases'
#             Height='height'
#             Weight='weight'
#             Allergies='allergies'
#             HistoryOfCancerInFamily='cancerInFamily'
#             NumberOfMajorSurgeries='surgeries'
#             Premium='premium'
#             Date=datetime()
#         )