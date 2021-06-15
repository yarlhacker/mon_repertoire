from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name= 'index'),
    path('detail/<int:id>/',views.detail , name= 'detail'),
    path('modifier/<int:id>/',views.modifier , name= 'modifier'),
    path('ajouter/',views.ajouter , name= 'ajouter'),
    path('supprimer/<int:id>/',views.supprimer , name= 'supprimer'),
    path('login/',views.login_views , name= 'login'),
    path('logout/',views.logout_view , name= 'logout'),
]
