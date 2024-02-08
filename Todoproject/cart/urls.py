from .import views
from django.urls import path
app_name='cart'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('removecart/',views.removecart,name='removecart'),
    path('fullremove/',views.fullremove,name='fullremove'),
    path('displaycart/',views.displaycart,name='displaycart'),
]
