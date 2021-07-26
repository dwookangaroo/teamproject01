from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_view, name='board_view'),
    path('usa/', views.usa_view, name='usa_view'),
    path('heinous/', views.heinous_view, name='heinous_view'),
]