from rest_framework import generics
from rest_framework.response import Response
from .models import Appointment, Patient
from .serializers import AppointmentSerializer, PatientSerializer
from rest_framework.permissions import AllowAny
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        patient_data = serializer.validated_data.pop('patient')
        appointment = serializer.save()
        Patient.objects.create(appointment=appointment, **patient_data)

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        patient_data = request.data.pop('patient')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        Patient.objects.filter(appointment=instance).update(**patient_data)
        return Response(serializer.data)
