from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter 

urlpatterns = [
    path('businesses/', views.BusinessList.as_view(), name='businesses_list'),
    path('businesses/<int:pk>', views.BusinessDetail.as_view(), name='businesses_detail')
]