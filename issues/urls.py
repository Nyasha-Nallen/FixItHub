from django.urls import path
from . import views

urlpatterns = [
    path('issues/', views.issue_list_create, name='issue-list-create'),
    path('issues/<int:pk>/', views.issue_detail, name='issue-detail'),
    path('categories/', views.category_list, name='category-list'),
]
