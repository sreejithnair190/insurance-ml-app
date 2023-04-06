from turtle import window_height
from django.db import models

# Create your models here.
class MedicalPremium(models.Model):
    Name = Diabetes = models.CharField(max_length = 100)
    Age = models.IntegerField()
    Diabetes = models.CharField(max_length = 10)
    BloodPressureProblems = models.CharField(max_length = 10)
    Transplants = models.CharField(max_length = 10)
    ChronicDiseases = models.CharField(max_length = 10)
    Height = models.FloatField()
    Weight = models.FloatField()
    Allergies = models.CharField(max_length = 10)
    HistoryOfCancerInFamily = models.CharField(max_length = 10)
    NumberOfMajorSurgeries = models.IntegerField()
    Premium = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    