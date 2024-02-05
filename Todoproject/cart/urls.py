from .import views
from django.urls import path
app_name='cart'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('displaycart/',views.displaycart,name='displaycart'),
]
