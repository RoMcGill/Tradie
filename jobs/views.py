from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .models import Customer, Job, Equipment, JobEquipment, Note, Photo, Quote, Invoice, Compliance
from .forms import CustomerForm, JobForm, EquipmentForm, NoteForm, PhotoForm, JobEquipmentForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'jobs/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('add_job', customer_id=customer.id)
    else:
        form = CustomerForm()
    return render(request, 'jobs/add_customer.html', {'form': form})

def add_job(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.customer = customer
            job.save()
            return redirect('add_note', job_id=job.id)
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form, 'customer': customer})

def add_note(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.job = job
            note.save()
            return redirect('add_photo', job_id=job.id)
    else:
        form = NoteForm()
    return render(request, 'jobs/add_note.html', {'form': form, 'job': job})

def add_photo(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.job = job
            photo.save()
            return redirect('select_equipment', job_id=job.id)
    else:
        form = PhotoForm()
    return render(request, 'jobs/add_photo.html', {'form': form, 'job': job})

def select_equipment(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    JobEquipmentFormSet = modelformset_factory(JobEquipment, form=JobEquipmentForm, extra=1)
    if request.method == 'POST':
        formset = JobEquipmentFormSet(request.POST, queryset=JobEquipment.objects.none())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.job = job
                instance.save()
            return redirect('generate_quote', job_id=job.id)
    else:
        formset = JobEquipmentFormSet(queryset=JobEquipment.objects.none())
        formset.form.base_fields['equipment'].queryset = Equipment.objects.all()
    return render(request, 'jobs/select_equipment.html', {'formset': formset, 'job': job})

def generate_quote(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    customer = job.customer
    tradesman = job.tradesman
    notes = Note.objects.filter(job=job)
    photos = Photo.objects.filter(job=job)
    job_equipment = JobEquipment.objects.filter(job=job)

    # Generate quote details
    total_cost = sum([item.equipment.price * item.quantity for item in job_equipment])
    equipment_details = ', '.join([f"{item.equipment.name} (x{item.quantity})" for item in job_equipment])

    quote = Quote.objects.create(job=job, equipment_details=equipment_details, total_cost=total_cost)
    quote.save()

    context = {
        'job': job,
        'customer': customer,
        'tradesman': tradesman,
        'notes': notes,
        'photos': photos,
        'job_equipment': job_equipment,
        'quote': quote,
    }

    return render(request, 'jobs/generate_quote.html', context)

def job_details_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    customer = job.customer
    tradesman = job.tradesman
    notes = Note.objects.filter(job=job)
    photos = Photo.objects.filter(job=job)
    job_equipment = JobEquipment.objects.filter(job=job)
    quotes = Quote.objects.filter(job=job)
    invoices = Invoice.objects.filter(job=job)
    compliance = Compliance.objects.filter(job=job).first()

    context = {
        'job': job,
        'customer': customer,
        'tradesman': tradesman,
        'notes': notes,
        'photos': photos,
        'job_equipment': job_equipment,
        'quotes': quotes,
        'invoices': invoices,
        'compliance': compliance,
    }

    return render(request, 'jobs/job_details.html', context)

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'jobs/equipment_list.html', {'equipment': equipment})

