from django.urls import path
from .import views as v
urlpatterns = [
    path("Add",v.addexpense,name="add"),
    path("List",v.expenselist,name="list"),
    path("delete/<int:id>",v.delete,name="delete"),
    path("edit/<int:id>",v.editexpense,name="edit"),
     path("search",v.search,name="search"),
    path("SortByExpense/<str:i>",v.sortbyexpense,name="sbe"),
]