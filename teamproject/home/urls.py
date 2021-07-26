from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('usa/', views.usa_view, name='usa_view'),
    path('recidivism/', views.recidivism_view, name='recidivism_view')
]