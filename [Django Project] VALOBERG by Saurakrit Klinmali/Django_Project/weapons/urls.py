from django.urls import path
from . import views

app_name = 'weapons'
urlpatterns = [
    path('', views.weapons_index, name="weapons_index"),
    path('skins', views.skins_index, name="skins_index"),
    path('<str:weapons_name>', views.weapons_detail, name="weapons_detail")
]
