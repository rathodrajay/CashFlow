from django.urls import path
from .import views as v
urlpatterns = [
    path("Add",v.addincome,name="add"),
    path("List",v.incomelist,name="list"),
    path("delete/<int:id>",v.delete,name="delete"),
    path("edit/<int:id>",v.editincome,name="edit"),
    path("search",v.search,name="search"),
    path("SortByIncome/<str:i>",v.sortbyincome,name="sbi"),
]