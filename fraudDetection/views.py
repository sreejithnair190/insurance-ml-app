from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
# Create your views here.
def FraudDetection(request):
    return render(request,'fraudDetection/fraud-detection.html')

def result(request):
    if request.method == 'POST' and 'Detect' in request.POST:
        temp = {}
        temp['capital-gains'] = request.POST.get('capital-gains')
        temp['capital-loss'] = request.POST.get('capital-loss')
        temp['incident_hour_of_the_day'] = request.POST.get('incident_hour_of_the_day')
        temp['witness'] = request.POST.get('witness')
        temp['total_claim_amount-loss'] = request.POST.get('total_claim_amount-loss')
        temp['number_of_vehicles_involved'] = request.POST.get('number_of_vehicles_involved')
        temp['insured_occupation'] = request.POST.get('insured_occupation')
        temp['insured_hobbies'] = request.POST.get('insured_hobbies')
        temp['incident_type'] = request.POST.get('incident_type')
        temp['collision_type'] = request.POST.get('collision_type')
        temp['incident_severity'] = request.POST.get('incident_severity')
        temp['authorities_contacted'] = request.POST.get('authorities_contacted')
        temp['age_group'] = request.POST.get('age_group')
        temp['months_as_customer_groups'] = request.POST.get('months_as_customer_groups')
        temp['policy_annual_premium_groups'] = request.POST.get('policy_annual_premium_groups')




        context={
            'temp':temp
        }
        return render(request,'fraudDetection/result.html',context)
