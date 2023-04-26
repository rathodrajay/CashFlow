from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import LoginForm
from django.contrib.auth import login,logout,authenticate
from income.models import Income
from expense.models import Expense
def homepage(request):
    d={"total":totalincexp(request)}
    return render(request,"home.html",d)

def addUser(request):
    if request.method=="POST":
        obj=UserCreationForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":UserCreationForm}
        return render(request,"form.html",d)

def checkuser(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else:
            return redirect("/Account-Login")
    else:
        d={"form":LoginForm}
        return render(request,"form.html",d)

def lgot(request):
    logout(request)
    return redirect("/")

def totalincexp(request):
    uid=request.session.get("uid")
    incomedata=Income.objects.filter(user=uid)
    expensedata=Expense.objects.filter(user=uid)
    ti=0
    te=0
    for i in incomedata:
        ti=ti+i.income
    for i in expensedata:
        te=te+i.expense

    return ti-te


