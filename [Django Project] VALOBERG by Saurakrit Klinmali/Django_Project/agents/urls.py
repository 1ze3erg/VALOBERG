from django.urls import path
from . import views

app_name = 'agents'
urlpatterns = [
    path('', views.agents_index, name="agents_index"),
    path('<str:agents_name>', views.agents_detail, name="agents_detail"),
    #path('<str:agents_name>', views.agents_ability, name="agents_ability")
] 

