from django.urls import path

from . import views

app_name = 'acceptance_aggregate'
urlpatterns = [
    path('repair/<int:repair_id>/acceptance_create',
         views.acceptance_aggregate_create,
         name='acceptance_aggregate_create'),
    path('repair/<int:repair_id>/acceptance_view',
         views.acceptance_aggregate_view,
         name='acceptance_aggregate_view'),
    path('repair/<int:repair_id>/acceptance/<int:acceptance_id>/edit',
         views.acceptance_aggregate_edit,
         name='acceptance_aggregate_edit'),
    path('repair/<int:repair_id>/acceptance/<int:acceptance_id>/delete',
         views.acceptance_aggregate_delete,
         name='acceptance_aggregate_delete'),
    path('repair/<int:repair_id>/acceptance/<int:acceptance_id>/img_view',
         views.acceptance_images_view,
         name='acceptance_images_view'),
    path(('repair/<int:repair_id>/acceptance/<int:acceptance_id>/'
         'single_image/<int:image_id>/edit'),
         views.single_image_edit,
         name='single_image_edit'),
]
