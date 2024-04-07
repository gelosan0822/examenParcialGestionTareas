from django.urls import path
from . import views

app_name='tareaApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('nuevaTarea',views.nuevaTarea,name='nuevaTarea')
]