from django.urls import path

from . import views

app_name = 'journal_repairs'
urlpatterns = [
    path('repair/', views.repair, name='repair'),
    path('repair_create/', views.repair_create, name='repair_create'),
    path('esn_create/', views.esn_create, name='esn_create'),
    path('esn_add/', views.esn_add, name='esn_add'),
    path('hours_add/', views.hours_add, name='hours_add'),
    path('repair/<int:repair_id>/', views.repair_detail, name='repair_detail'),
    path(
        'repair/<int:repair_id>/comment/',
        views.add_comment,
        name='add_comment'),
    path('repair/<int:repair_id>/edit/',
         views.repair_edit, name='repair_edit'),
    path('esn/<int:esn_id>/edit/<int:repair_id>/',
         views.esn_edit, name='esn_edit'),
    path('esn/<slug:slug>/', views.esn_repairs, name='esn_repairs'),
    path('customer/<slug:slug>/',
         views.customer_repairs, name='customer_repairs'),
    path('search/', views.search, name='search'),
    path('esn_search/', views.esn_search, name='esn_search'),
]
