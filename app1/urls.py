from django.urls import path
from app1.views import*

app_name='something1'

urlpatterns=[
    path('tarun/',tarun,name='tarun'),
    path('varsha/',varsha,name='varsha'),
]