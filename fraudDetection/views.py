from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def FraudDetection(request):
    return render(request,'fraudDetection/fraud-detection.html')


def fraud_result(request):
    if request.method == 'POST' and 'Detect' in request.POST:
        sc = StandardScaler()
        svc_tuned = pickle.load(open("svc_tuned_fraud_detection.pkl", "rb"))
        temp = {}
        temp['capital-gains'] = request.POST.get('capital-gains')
        temp['capital-loss'] = request.POST.get('capital-loss')
        temp['incident_hour_of_the_day'] = request.POST.get('incident_hour_of_the_day')
        temp['number_of_vehicles_involved'] = request.POST.get('number_of_vehicles_involved')
        temp['witnesses'] = request.POST.get('witness')
        temp['total_claim_amount'] = request.POST.get('total_claim_amount')

        # Assigning Values for gender
        temp['insured_sex_FEMALE'] = 0
        temp['insured_sex_MALE'] = 0
        if request.POST.get('insured_sex') == "female":
            temp['insured_sex_FEMALE'] = 1
        else:
            temp['insured_sex_MALE'] = 1

        # Assigning Values for occupation
        temp['insured_occupation_adm-clerical'] = 0
        temp['insured_occupation_armed-forces'] = 0
        temp['insured_occupation_craft-repair'] = 0
        temp['insured_occupation_exec-managerial'] = 0
        temp['insured_occupation_farming-fishing'] = 0
        temp['insured_occupation_handlers-cleaners'] = 0
        temp['insured_occupation_machine-op-inspct'] = 0
        temp['insured_occupation_priv-serv'] = 0
        temp['insured_occupation_prof-specialty'] = 0
        temp['insured_occupation_protective-serv'] = 0
        temp['insured_occupation_sales'] = 0
        temp['insured_occupation_tech-support'] = 0
        temp['insured_occupation_transport-moving'] = 0
        temp['insured_occupation_other-service'] = 0

        occupation = request.POST.get('insured_occupation')
        if occupation == "insured_occupation_adm-clerical":
            temp['insured_occupation_adm-clerical'] = 1
        elif occupation == "insured_occupation_armed-forces":
            temp['insured_occupation_armed-forces'] = 1
        elif occupation == "insured_occupation_craft-repair":
            temp['insured_occupation_craft-repair'] = 1
        elif occupation == "insured_occupation_exec-managerial":
            temp['insured_occupation_exec-managerial'] = 1
        elif occupation == "insured_occupation_farming-fishing":
            temp['insured_occupation_farming-fishing'] = 1
        elif occupation == "insured_occupation_handlers-cleaners":
            temp['insured_occupation_handlers-cleaners'] = 1
        elif occupation == "insured_occupation_machine-op-inspct":
            temp['insured_occupation_machine-op-inspct'] = 1
        elif occupation == "insured_occupation_priv-house-serv":
            temp['insured_occupation_priv-serv'] = 1
        elif occupation == "insured_occupation_prof-specialty":
            temp['insured_occupation_prof-specialty'] = 1
        elif occupation == "insured_occupation_protective-serv":
            temp['insured_occupation_protective-serv'] = 1
        elif occupation == "insured_occupation_sales":
            temp['insured_occupation_sales'] = 1
        elif occupation == "insured_occupation_tech-support":
            temp['insured_occupation_tech-support'] = 1
        elif occupation == "insured_occupation_transport-moving":
            temp['insured_occupation_transport-moving'] = 1
        elif occupation == "insured_occupation_other-service":
            temp['insured_occupation_other-service'] = 1

        # Assigning Values for hobbies
        temp['insured_hobbies_base-jumping'] = 0
        temp['insured_hobbies_basketball'] = 0
        temp['insured_hobbies_board-games'] = 0
        temp['insured_hobbies_bungie-jumping'] = 0
        temp['insured_hobbies_camping'] = 0
        temp['insured_hobbies_chess'] = 0
        temp['insured_hobbies_cross-fit'] = 0
        temp['insured_hobbies_dancing'] = 0
        temp['insured_hobbies_exercise'] = 0
        temp['insured_hobbies_golf'] = 0
        temp['insured_hobbies_hiking'] = 0
        temp['insured_hobbies_kayaking'] = 0
        temp['insured_hobbies_movies'] = 0
        temp['insured_hobbies_paintball'] = 0
        temp['insured_hobbies_polo'] = 0
        temp['insured_hobbies_reading'] = 0
        temp['insured_hobbies_skydiving'] = 0
        temp['insured_hobbies_sleeping'] = 0
        temp['insured_hobbies_video-games'] = 0
        temp['insured_hobbies_yachting'] = 0

        hobbies = request.POST.get('insured_hobbies')
        if hobbies == 'base-jumping':
            temp['insured_hobbies_base-jumping'] = 1
        elif hobbies == 'basketball':
            temp['insured_hobbies_basketball'] = 1
        elif hobbies == 'board-games':
            temp['insured_hobbies_board-games'] = 1
        elif hobbies == 'bungie-jumping':
            temp['insured_hobbies_bungie-jumping'] = 1
        elif hobbies == 'camping':
            temp['insured_hobbies_camping'] = 1
        elif hobbies == 'chess':
            temp['insured_hobbies_chess'] = 1
        elif hobbies == 'cross-fit':
            temp['insured_hobbies_cross-fit'] = 1
        elif hobbies == 'dancing':
            temp['insured_hobbies_dancing'] = 1
        elif hobbies == 'exercise':
            temp['insured_hobbies_exercise'] = 1
        elif hobbies == 'golf':
            temp['insured_hobbies_golf'] = 1
        elif hobbies == 'hiking':
            temp['insured_hobbies_hiking'] = 1
        elif hobbies == 'kayaking':
            temp['insured_hobbies_kayaking'] = 1
        elif hobbies == 'movies':
            temp['insured_hobbies_movies'] = 1
        elif hobbies == 'paintball':
            temp['insured_hobbies_paintball'] = 1
        elif hobbies == 'polo':
            temp['insured_hobbies_polo'] = 1
        elif hobbies == 'reading':
            temp['insured_hobbies_reading'] = 1
        elif hobbies == 'skydiving':
            temp['insured_hobbies_skydiving'] = 1
        elif hobbies == 'hobbies-other' or hobbies == 'sleeping' :
            temp['insured_hobbies_sleeping'] = 1
        elif hobbies == 'video-games':
            temp['insured_hobbies_video-games'] = 1
        elif hobbies == 'yatching':
            temp['insured_hobbies_yachting'] = 1

        # Assigning values for incident type
        temp['incident_type_Multi-vehicle Collision'] = 0
        temp['incident_type_Parked Car'] = 0
        temp['incident_type_Single Vehicle Collision'] = 0
        temp['incident_type_Vehicle Theft'] = 0

        incident_type = request.POST.get('incident_type')
        if incident_type == 'Multi-vehicle':
            temp['incident_type_Multi-vehicle Collision'] = 1
        elif incident_type == 'Parked-Car':
            temp['incident_type_Parked Car'] = 1
        elif incident_type == 'Single-Vehicle':
            temp['incident_type_Single Vehicle Collision'] = 1
        elif incident_type == 'Vehicle-Theft':
            temp['incident_type_Vehicle Theft'] = 1

        # Assigning values for collision type
        temp['collision_type_?'] = 0
        temp['collision_type_Front Collision'] = 0
        temp['collision_type_Rear Collision'] = 0
        temp['collision_type_Side Collision'] = 0

        collision_type = request.POST.get('collision_type')
        if collision_type == 'Front Collision':
            temp['collision_type_Front Collision'] = 1
        elif collision_type == 'Rear Collision':
            temp['collision_type_Rear Collision'] = 1
        elif collision_type == 'Side Collision':
            temp['collision_type_Side Collision'] = 1

        # Assigning values for incident severity
        temp['incident_severity_Major Damage'] = 0
        temp['incident_severity_Minor Damage'] = 0
        temp['incident_severity_Total Loss'] = 0
        temp['incident_severity_Trivial Damage'] = 0

        incident_severity = request.POST.get('incident_severity')

        if incident_severity == 'Major Damage':
            temp['incident_severity_Major Damage'] = 1
        elif incident_severity == 'Minor Damage':
            temp['incident_severity_Minor Damage'] = 1
        elif incident_severity == 'Total loss':
            temp['incident_severity_Total Loss'] = 1
        elif incident_severity == 'Trivial Damage':
            temp['incident_severity_Trivial Damage'] = 1

        # Assigning values for Authorities Contacted
        temp['authorities_contacted_Ambulance'] = 0
        temp['authorities_contacted_Police'] = 0
        temp['authorities_contacted_Fire'] = 0
        temp['authorities_contacted_Other'] = 0
        temp['authorities_contacted_None'] = 0

        authorities_contacted = request.POST.get('authorities_contacted')
        if authorities_contacted == "Ambulance":
            temp['authorities_contacted_Ambulance'] = 1
        elif authorities_contacted == "Fire":
            temp['authorities_contacted_Fire'] = 1
        elif authorities_contacted == "Police":
            temp['authorities_contacted_Police'] = 1
        elif authorities_contacted == "Other":
            temp['authorities_contacted_Other'] = 1
        elif authorities_contacted == "None":
            temp['authorities_contacted_None'] = 1

        # Assigning values for Age Group
        temp['age_group_15-20'] = 0
        temp['age_group_21-25'] = 0
        temp['age_group_26-30'] = 0
        temp['age_group_31-35'] = 0
        temp['age_group_36-40'] = 0
        temp['age_group_41-45'] = 0
        temp['age_group_46-50'] = 0
        temp['age_group_51-55'] = 0
        temp['age_group_56-60'] = 0
        temp['age_group_61-65'] = 0

        age_group = request.POST.get('age_group')

        if age_group == '15-20':
            temp['age_group_15-20'] = 1
        elif age_group == '21-25':
            temp['age_group_21-25'] = 1
        elif age_group == '26-30':
            temp['age_group_26-30'] = 1
        elif age_group == '31-35':
            temp['age_group_31-35'] = 1
        elif age_group == '36-40':
            temp['age_group_36-40'] = 0
        elif age_group == '41-45':
            temp['age_group_41-45'] = 1
        elif age_group == '46-50':
            temp['age_group_46-50'] = 1
        elif age_group == '51-55':
            temp['age_group_51-55'] = 1
        elif age_group == '56-60':
            temp['age_group_56-60'] = 1
        elif age_group == '61-65':
            temp['age_group_61-65'] = 1

        # Assigning values for Age Group
        temp['months_as_customer_groups_0-50'] = 0
        temp['months_as_customer_groups_51-100'] = 0
        temp['months_as_customer_groups_101-150'] = 0
        temp['months_as_customer_groups_151-200'] = 0
        temp['months_as_customer_groups_201-250'] = 0
        temp['months_as_customer_groups_251-300'] = 0
        temp['months_as_customer_groups_301-350'] = 0
        temp['months_as_customer_groups_351-400'] = 0
        temp['months_as_customer_groups_401-450'] = 0
        temp['months_as_customer_groups_451-500'] = 0

        months_as_customer = request.POST.get('months_as_customer_groups')

        if months_as_customer == '51-100':
            temp['months_as_customer_groups_0-50'] = 1
        elif months_as_customer == '51-100':
            temp['months_as_customer_groups_51-100'] = 1
        elif months_as_customer == '101-150':
            temp['months_as_customer_groups_101-150'] = 1
        elif months_as_customer == '151-200':
            temp['months_as_customer_groups_151-200'] = 1
        elif months_as_customer == '201-250':
            temp['months_as_customer_groups_201-250'] = 1
        elif months_as_customer == '251-300':
            temp['months_as_customer_groups_251-300'] = 1
        elif months_as_customer == '301-350':
            temp['months_as_customer_groups_301-350'] = 1
        elif months_as_customer == '351-400':
            temp['months_as_customer_groups_351-400'] = 1
        elif months_as_customer == '401-450':
            temp['months_as_customer_groups_401-450'] = 1
        elif months_as_customer == '451-500':
            temp['months_as_customer_groups_451-500'] = 1

        # Assigning values for Age Group
        temp['policy_annual_premium_groups_low'] = 0
        temp['policy_annual_premium_groups_medium'] = 0
        temp['policy_annual_premium_groups_high'] = 0
        temp['policy_annual_premium_groups_very high'] = 0
        temp['policy_annual_premium_groups_very low'] = 0

        policy_annual_premium_groups = request.POST.get('policy_annual_premium_groups')

        if policy_annual_premium_groups == 'low':
            temp['policy_annual_premium_groups_low'] = 1
        elif policy_annual_premium_groups == 'medium':
            temp['policy_annual_premium_groups_medium'] = 1
        elif policy_annual_premium_groups == 'high':
            temp['policy_annual_premium_groups_high'] = 1
        elif policy_annual_premium_groups == 'very-high':
            temp['policy_annual_premium_groups_very high'] = 1
        elif policy_annual_premium_groups == 'very-low':
            temp['policy_annual_premium_groups_very low'] = 1

        temp_df = pd.DataFrame(temp, index=[0])
        # X = temp_df.iloc[[0]]
        test_data = sc.fit_transform(temp_df)
        predict = svc_tuned.predict(test_data)

        context={
                'temp':temp,
                'result':predict
            }
    return render(request,'fraudDetection/result.html',context)
