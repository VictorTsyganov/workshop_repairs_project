from django.urls import path

from . import views

app_name = 'journal_repairs'
urlpatterns = [
    path('journal/', views.journal, name='journal'),
]