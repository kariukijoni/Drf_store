from django.urls import path
# from django.views import item_list\
from . import views

urlpatterns = [
    path('items/',views.ItemList.as_view()),
    path('items/<int:pk>/',views.ItemDetail.as_view())
]
