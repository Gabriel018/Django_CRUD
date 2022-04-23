from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('cliente',views.clientes,name='clientes'),
path('add_form',views.add_form, name='add_form'),
path('client_add',views.client_add,name='client_add'),
path('delete/<int:id>',views.delete,name='delete'),
]
