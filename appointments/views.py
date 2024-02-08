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

class AppointmentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            # Filter appointments based on query parameters
            search_query = request.query_params.get('q', '')
            appointments = Appointment.objects.filter(
                 problem__icontains=search_query,
    department__icontains=search_query,
    doctor__icontains=search_query,
    patient__patient_name_english__icontains=search_query,
    patient__patient_name_bangla__icontains=search_query
            ).order_by('-created_at')

            # Pagination
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('pageSize', 5))
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            appointments = appointments[start_index:end_index]

            serializer = AppointmentSerializer(appointments, many=True)
            total_appointments = Appointment.objects.count()

            return Response(
                {
                    'totalAppointments': total_appointments,
                    'appointments': serializer.data,
                    'message': 'Success',
                },
                status=200,
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'totalAppointments': 0,
                    'appointments': [],
                    'message': 'Internal Server Error',
                },
                status=500,
            )
