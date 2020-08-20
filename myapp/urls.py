from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('introduce/', views.introduce, name="introduce"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('update/<int:designer_id>/', views.update, name="update"),
]