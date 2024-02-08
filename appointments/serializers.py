# appointments/serializers.py
from rest_framework import serializers
from .models import Appointment, Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_set = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
