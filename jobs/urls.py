from django.urls import path
from .views import add_customer, customer_list, add_job, add_note, add_photo, select_equipment, generate_quote, job_details_view, job_list, equipment_list

urlpatterns = [
    path('add_customer/', add_customer, name='add_customer'),
    path('customers/', customer_list, name='customer_list'),
    path('add_job/<int:customer_id>/', add_job, name='add_job'),
    path('add_note/<int:job_id>/', add_note, name='add_note'),
    path('add_photo/<int:job_id>/', add_photo, name='add_photo'),
    path('select_equipment/<int:job_id>/', select_equipment, name='select_equipment'),
    path('generate_quote/<int:job_id>/', generate_quote, name='generate_quote'),
    path('jobs/<int:job_id>/', job_details_view, name='job_details'),
    path('jobs/', job_list, name='job_list'),
    path('equipment/', equipment_list, name='equipment_list'),
]
