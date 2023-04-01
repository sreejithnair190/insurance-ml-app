from django.urls import path
from . import views
urlpatterns =[
    path("",views.MedicalCost),
    path("result",views.result),
]
