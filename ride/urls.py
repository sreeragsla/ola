from ride.views import *
from django.urls import path
app_name='something'

urlpatterns=[
    path('auto/',auto,name='auto'),
]