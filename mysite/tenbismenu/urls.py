from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/', views.drinks, name='drinks'),
    path('drink/<int:id>/', views.specDrink, name='specDrink'),
    path('pizzas/', views.pizza, name='pizza'),
    path('pizza/<int:id>/', views.specPizza, name='specPizza'),
    path('desserts/', views.desserts, name='desserts'),
    path('dessert/<int:id>/', views.specDessert, name='specDessert'),

    
]