from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('tradesman', 'Tradesman'),
    ]
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tradesman = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.status}"

class Note(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note[:20]

class Photo(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for job {self.job.id}"

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class JobEquipment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.equipment.name} for job {self.job.id}"

class Quote(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    equipment_details = models.TextField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote for job {self.job.id}"

class Invoice(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    invoice_details = models.TextField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for job {self.job.id}"

class Compliance(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    law_info = models.TextField(blank=True, null=True)
    standard_info = models.TextField(blank=True, null=True)
    tax_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compliance for job {self.job.id}"
