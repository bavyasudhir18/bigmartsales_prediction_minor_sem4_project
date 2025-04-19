from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salesdata/', views.salesdata_list, name='salesdata_list'),
    path('salesdata/add/', views.salesdata_add, name='salesdata_add'),
    path('salesdata/edit/<int:pk>/', views.salesdata_edit, name='salesdata_edit'),
    path('salesdata/delete/<int:pk>/', views.salesdata_delete, name='salesdata_delete'),
    path('', views.index, name='home'),  # Dashboard view
    path('train-data/', views.train_data_list, name='train_data_list'),  # CSV table
]
