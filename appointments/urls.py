# urls.py
from django.urls import path
from .views import (
    CreateAppointment
    # AppointmentListCreateAPIView,
    # AppointmentRetrieveUpdateAPIView,
    # PatientListCreateAPIView,
    # PatientRetrieveUpdateAPIView,
)

urlpatterns = [
    path('appointments/', CreateAppointment.as_view(), name='appointment-list-create'),
    # path('appointments/<int:pk>/', AppointmentRetrieveUpdateAPIView.as_view(), name='appointment-retrieve-update'),
    # path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    # path('patients/<int:pk>/', PatientRetrieveUpdateAPIView.as_view(), name='patient-retrieve-update'),
]
