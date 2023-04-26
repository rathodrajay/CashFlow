from django.db import models
from django.contrib.auth.models import User
from django import forms
class Income(models.Model):
    # id = models.BigIntegerField()
    income=models.IntegerField()
    income_type=models.CharField(max_length=30)
    income_date=models.DateField(auto_now=True)
    description=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="Income"

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields="__all__"
