# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:41:05 2020

@author: Daan
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]