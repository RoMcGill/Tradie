from django import forms
from .models import Customer, Job, Equipment, Note, Photo, JobEquipment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_info', 'address']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['customer', 'tradesman', 'status']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'price', 'supplier_id']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['job', 'note']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['job', 'photo']

class JobEquipmentForm(forms.ModelForm):
    class Meta:
        model = JobEquipment
        fields = ['equipment', 'quantity']
