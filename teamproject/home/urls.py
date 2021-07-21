from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_view, name='board_view'),
    path('compare/', views.compare_view, name='compare_view')
]