from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_view, name='board_view'),

    path('usa/', views.usa_view, name='usa_view'),
    path('heinous/', views.heinous_view, name='heinous_view'),
    path('recidivism/', views.recidivism_view, name='recidivism_view'),
    path('compare/', views.compare_view, name='compare_view'),
    path('motive/', views.motive_view, name='motive_view')

]