# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from .models import Appointment, Patient
from .serializers import AppointmentSerializer, PatientSerializer
from rest_framework.permissions import AllowAny
class CreateAppointment(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        appointment_data = request.data

        appointment_serializer = AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            # Start a transaction
            with transaction.atomic():
                appointment_instance = appointment_serializer.save()

                # Extract patient data and set appointment instance
                patient_data = appointment_data.copy()
                patient_data['appointment'] = appointment_instance.id

                patient_serializer = PatientSerializer(data=patient_data)
                if patient_serializer.is_valid():
                    patient_serializer.save()
                    return Response(appointment_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    # Rollback appointment creation if patient creation fails
                    appointment_instance.delete()
                    return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # permission_classes = [AllowAny]