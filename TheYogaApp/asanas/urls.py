from django.urls import path
from . import views
import pickle
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('yoga/', views.yoga, name='yoga'),
    path('heart/',views.heart,name='heart'),
    path('diabetes/',views.diabetes,name='diabetes')
    
    
]
