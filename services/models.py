from django.db import models

# Create your models here.
# 1. birthchart reading request
class BirthChartRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    question = models.TextField(blank=True, null=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f"Birth chart for {self.full_name} ({self.email})"return f"Birth chart for {self.full_name} ({self.email})"