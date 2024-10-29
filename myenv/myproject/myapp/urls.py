from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('counter', views.counter, name='counter'),
    path('date-picker/', views.example_view, name='example_view'),
    path('employee/', views.employee_view, name="employee"),
]
