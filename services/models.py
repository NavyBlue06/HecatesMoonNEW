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
    
    # 2. Ask a witch request
class WitchQuestion(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question from {self.full_name}"  

# 3. Ritual or spell request
class RitualRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    intention = models.CharField(max_length=200)
    details = models.TextField()
    urgency = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ritual request from {self.full_name} - {self.intention}"  