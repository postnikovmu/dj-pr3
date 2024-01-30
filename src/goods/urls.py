from django.urls import path, re_path
from . import views

urlpatterns = [
    path('get_token/', views.get_token, name='get_token'),
    re_path(r'^goods/?', views.goods, name='goods'),
    re_path(r'^new_good/?', views.new_good, name='new_good'),
]
