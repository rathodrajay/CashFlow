from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User

def total(request):
    ids=request.session.get("uid")
    data=Income.objects.filter(user=ids)
    t=0
    for i in data:
        t=t+i.income
    return t

def addincome(request):
    uid=request.session.get("uid")
    if request.method=="POST":
        income=request.POST.get("income")
        income_type=request.POST.get("income_type")
        description=request.POST.get("description")
        obj=Income()
        obj.income=income
        obj.income_type=income_type
        obj.description=description
        obj.user=User.objects.get(id=uid)
        obj.save()
        return redirect("/")
    else:
        return render(request,"addincome.html")

def incomelist(request):
    uid=request.session.get("uid")
    data=Income.objects.filter(user=uid)
    # d={"obj":data}
    s=set()
    data2=Income.objects.filter(user=uid)
    for i in data2:
        s.add(i.income_type)
    t = total(request)
    print(t)
    d={"obj":data,"incl":s,"total":total(request)}
    print(s)
    return render(request,"incomelist.html",d)

def delete(request,id):
    obj=Income.objects.get(id=id)
    obj.delete()
    return redirect("/Income-List")

def editincome(request,id):
    obj=Income.objects.get(id=id)
    if request.method=="POST":
        obj.income=request.POST["income"]
        obj.income_type=request.POST["income_type"]
        obj.description=request.POST["description"]
        obj.save(update_fields=['income','income_type','description'])
        return redirect("/Income-List")
    else:
        return render(request,"editincome.html",{'i':obj,})

def search(request):
    ids=request.session.get("uid")
    srch=request.POST.get("srch")
    s=set()
    data=Income.objects.filter(user=ids,income_type__contains=srch)
    data2=Income.objects.filter(user=ids)
    for i in data2:
        s.add(i.income_type)
    d={"obj":data,"incl":s}
    return render(request,"incomelist.html",d)

def sortbyincome(request,i):
    ids=request.session.get("uid")
    data=Income.objects.filter(user=ids,income_type=i)
    t=0
    for i in data:
        t=t+i.income
    s=set()
    data2=Income.objects.filter(user=ids)
    for i in data2:
        s.add(i.income_type)
    d={"obj":data,"incl":s,"total":t}
    return render(request,"incomelist.html",d)








    

