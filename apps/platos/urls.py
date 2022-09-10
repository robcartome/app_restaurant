from django.urls import path
from . import views

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('', views.plato_details, name='plato_detail'),
    path('plato_search/', views.plato_search, name='plato_search'),

    # REST
    path('plato_detail_drf_def/<int:pk>/', views.plato_detail_view, name='plato_detail_rf_def'),
]