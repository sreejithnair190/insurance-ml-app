from django.urls import path
from . import views
urlpatterns =[
    path("",views.FraudDetection),
    # path("result",views.result),
    # path('save-to-db', views.save_to_db, name='saveToDB'),
]