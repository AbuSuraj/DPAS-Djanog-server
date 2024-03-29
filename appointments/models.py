# models.py
from django.db import models

class Appointment(models.Model):
    problem = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Appointment ID: {self.pk}"

class Patient(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient_name_english = models.CharField(max_length=255)
    patient_name_bangla = models.CharField(max_length=255)
    patient_father_name_english = models.CharField(max_length=255)
    patient_father_name_bangla = models.CharField(max_length=255)
    patient_mother_name_english = models.CharField(max_length=255)
    patient_mother_name_bangla = models.CharField(max_length=255)
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    nid_or_birth_certificate_no = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Patient ID: {self.pk}"
