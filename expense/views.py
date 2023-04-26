from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from account.views import totalincexp

def total(request):
    ids=request.session.get("uid")
    data=Expense.objects.filter(user=ids)
    t=0
    for i in data:
        t=t+i.expense
    return t

def addexpense(request):
    uid=request.session.get("uid")
    if request.method=="POST":
        expense=request.POST.get("expense")
        expense_type=request.POST.get("expense_type")
        description=request.POST.get("description")
        obj=Expense()
        obj.expense=expense
        obj.expense_type=expense_type
        obj.description=description
        obj.user=User.objects.get(id=uid)
        expenseamt=request.POST.get("expense")
        balance=totalincexp(request)
        print(balance)
        print(expenseamt)
        rb=balance-int(expenseamt)
        if rb<0:
            d={"msg":"your enter expense amt is not valid ","form":ExpenseForm}
            return render(request,"addexpense.html",d)
        obj.save()
        return redirect("/")

    else:
        return render(request,"addexpense.html")


def expenselist(request):
    uid=request.session.get("uid")
    data=Expense.objects.filter(user=uid)
    s=set()
    data2=Expense.objects.filter(user=uid)
    for i in data2:
        s.add(i.expense_type)
    t = total(request)
    print(t)
    d={"obj":data,"incl":s,"total":total(request)}
    print(s)
    return render(request,"expenselist.html",d)

def delete(request,id):
    obj=Expense.objects.get(id=id)
    obj.delete()
    return redirect("/Income-List")

def editexpense(request,id):
    obj=Expense.objects.get(id=id)
    if request.method=="POST":
        obj.expense=request.POST["expense"]
        obj.expense_type=request.POST["expense_type"]
        obj.description=request.POST["description"]
        obj.save(update_fields=['expense','expense_type','description'])
        return redirect("/Expense-List")
    else:
        return render(request,"editexpense.html",{'i':obj,})

def search(request):
    ids=request.session.get("uid")
    srch=request.POST.get("srch")
    s=set()
    data=Expense.objects.filter(user=ids,description__contains=srch)
    data2=Expense.objects.filter(user=ids)
    for i in data2:
        s.add(i.expense_type)
    d={"obj":data,"incl":s}
    return render(request,"expenselist.html",d)

def sortbyexpense(request,i):
    ids=request.session.get("uid")
    data=Expense.objects.filter(user=ids,expense_type=i)
    t=0
    for i in data:
        t=t+i.expense
    s=set()
    data2=Expense.objects.filter(user=ids)
    for i in data2:
        s.add(i.expense_type)
    d={"obj":data,"incl":s,"total":t}
    return render(request,"expenselist.html",d)

