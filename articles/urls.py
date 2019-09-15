from django.urls import path
from . import views

# domain.com/pages/___
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:article_pk>/delete/', views.delete),
    path('<int:article_pk>/edit/', views.edit),
    path('<int:article_pk>/update/', views.update),
]
