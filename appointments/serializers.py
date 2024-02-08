from rest_framework import serializers
from .models import Appointment, Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        appointment = Appointment.objects.create(**validated_data)
        Patient.objects.create(appointment=appointment, **patient_data)
        return appointment

    def update(self, instance, validated_data):
        patient_data = validated_data.pop('patient')
        instance = super().update(instance, validated_data)
        Patient.objects.filter(appointment=instance).update(**patient_data)
        return instance
