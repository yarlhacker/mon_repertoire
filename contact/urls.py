from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name= 'index'),
    path('detail/',views.detail , name= 'detail'),
    path('modifier/',views.modifier , name= 'modifier'),
    path('ajouter/',views.ajouter , name= 'ajouter'),
]
