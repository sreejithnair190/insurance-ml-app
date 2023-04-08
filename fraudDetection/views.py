from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
# Create your views here.
def FraudDetection(response):
    return render(response,'fraudDetection/fraud-detection.html')