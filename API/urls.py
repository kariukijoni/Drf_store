from django.urls import path
# from django.views import item_list\
from . import views

urlpatterns = [
    path('items/',views.item_list),
    path('snippets/<int:pk>/',views.item_detail)
]
