# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:41:05 2020

@author: Daan
"""

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [    
    path('', views.IndexView.as_view(), name='index'),
    path('topics/', views.topics, name='topics'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]