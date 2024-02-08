# appointments/views.py
from rest_framework import generics
from .models import Appointment, Patient
from .serializers import AppointmentSerializer, PatientSerializer

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
