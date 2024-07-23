from django.contrib import admin
from django.urls import path,include
from olcha.views import CategoryListView,CategoryDetailView


urlpatterns = [
    path('categories/',CategoryListView.as_view(), name = 'category-list'),
    # path('detail/<slug-slug>/',CategoryDetailView.as_view(),name = 'category_detail')

]
