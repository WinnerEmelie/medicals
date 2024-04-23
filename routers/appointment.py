from fastapi import APIRouter

from schema.appointment import Appointments, AppointmentsCreate
from schema.patient import PatientsCreate, Patients
from services.appointment import AppointmentService
from services.patient import PatientService

from schema.doctor import DoctorsCreate, Doctors
from services.doctor import DoctorService

patient_router = APIRouter()

doctor_router = APIRouter()
appointment_router= APIRouter()

@appointment_router.post('', status_code=201)
def create_appointment( AppointmentCreate):
    data = AppointmentService.create_appointment
    return {'message': 'success', 'data': data}

@appointment_router.get('', status_code=200)
def get_appointment():
    return {'message': 'success', 'data': Appointments}

@appointment_router.get('/{appointment_id}')
def get_appointment_by_id(appointment_id: int):
    data = AppointmentService.get_flight_by_id(appointment_id)
    return {'message': 'success',  'data': data}

@appointment_router.put('/{appointment_id}')
def update_appointment(appointment_id: int, payload: AppointmentsCreate):
    data = AppointmentService.update_appointment(appointment_id, payload)
    return {'message': 'unavailable', 'data': data}

@appointment_router.delete('/{appointment_id}', status_code=200)
def delete_appointment(appointment_id: int):
    AppointmentService.delete_appointment(appointment_id)
    return {'Appointment deleted successfully.'}