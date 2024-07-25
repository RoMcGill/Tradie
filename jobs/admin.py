# jobs/admin.py

from django.contrib import admin
from .models import User, Customer, Job, Note, Photo, Equipment, JobEquipment, Quote, Invoice, Compliance

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Note)
admin.site.register(Photo)
admin.site.register(Equipment)
admin.site.register(JobEquipment)
admin.site.register(Quote)
admin.site.register(Invoice)
admin.site.register(Compliance)
