from  django.urls import path
from  .views import *
urlpatterns = [      # создаём переменную
    path('', index)   #при переходе на первую страницу обрабатывается "index"
]