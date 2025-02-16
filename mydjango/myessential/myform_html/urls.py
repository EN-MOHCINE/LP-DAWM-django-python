from django.urls import path
from . import views

app_name = 'myform_html'
urlpatterns = [
    path('add/', views.add_car, name='add_car'),
    path('list/', views.list_cars, name='list_cars'),
    path('delete/', views.delete_car, name='delete_car'),
]