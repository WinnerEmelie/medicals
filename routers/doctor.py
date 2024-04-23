from fastapi import APIRouter

from schema.doctor import DoctorsCreate, doctor          
from services.doctor import DoctorService

doctor_router = APIRouter()

@doctor_router.post('', status_code=201)
def create_doctor(payload: DoctorsCreate):
    data = DoctorService.create_doctor(payload)
    return {'message': 'success', 'data': data}

@doctor_router.get('', status_code=200)
def get_doctors():
    return {'message': 'success', 'data': doctor}

@doctor_router.get('/{doctor_id}')
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'success',  'data': data}

@doctor_router.put('/{doctor_id}')
def edit_doctor(doctor_id: int, payload: DoctorsCreate):
    data = DoctorService.edit_doctor(doctor_id, payload)
    return {'message': 'success', 'data': data}

@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(flight_id: int):
    DoctorService.delete_doctor(doctor)
    return {'account deleted successfully.'}
