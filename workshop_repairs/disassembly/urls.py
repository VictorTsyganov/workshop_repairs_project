from django.urls import path

from . import views

app_name = 'disassembly'
urlpatterns = [
    path('repair/<int:repair_id>/crankshaft_view',
         views.crankshaft_view,
         name='crankshaft_view'),
    path('repair/<int:repair_id>/crankshaft_create',
         views.crankshaft_create,
         name='crankshaft_create'),
    path('repair/<int:repair_id>/crankshaft_create_list2/<int:esn_id>',
         views.crankshaft_create_list2,
         name='crankshaft_create_list2'),
    path('repair/<int:repair_id>/crankshaft_view/<int:esn_id>/detail',
         views.crankshaft_view_detail,
         name='crankshaft_view_detail'),
    path('repair/<int:repair_id>/crankshaft_view/<int:esn_id>/delete',
         views.crankshaft_delete,
         name='crankshaft_delete'),
    path(('repair/<int:repair_id>/crankshaft_view/<int:esn_id>/'
         'single_image/<int:image_id>/edit'),
         views.single_image_edit,
         name='single_image_edit'),
    path('repair/<int:repair_id>/crankshaft_view/<int:esn_id>/edit',
         views.crankshaft_edit,
         name='crankshaft_edit'),
    path('repair/<int:repair_id>/crankshaft_view/<int:esn_id>/edit_list2',
         views.crankshaft_list2_edit,
         name='crankshaft_list2_edit'),
]
