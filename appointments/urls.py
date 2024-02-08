# urls.py
from django.urls import path
from .views import CreateAppointment, AppointmentListView

urlpatterns = [
    path('appointments/', CreateAppointment.as_view(), name='create-appointment'),
    path('appointments/list/', AppointmentListView.as_view(), name='appointment-list'),
]
