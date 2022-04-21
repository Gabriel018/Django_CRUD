from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('cliente',views.clientes,name='clientes'),
path('delete/<int:id>',views.delete,name='delete')
]
