from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_application, name='loan_application'),
]

