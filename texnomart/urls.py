from django.contrib import admin
from django.urls import path,include
from texnomart.views import ProductListApi


urlpatterns = [
    path('',ProductListApi.as_view(), name = 'product-list')

]
