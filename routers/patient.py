from fastapi import APIRouter, Response

from schema.patient import patients, PatientsCreateEdit
from services.patient import PatientSerivce

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    data = PatientSerivce.parse_patients(patient_data=patients)
    return {'message': 'successful', 'data': data}

@patient_router.get('/{patient_id}', status_code=200)
def get_patient_by_id(patient_id: int):
    data =  PatientSerivce.get_patient_by_id(patient_id)
    return {'message': 'successful', 'data': data} 

@patient_router.post('/', status_code=201)
def create_patient(payload: PatientsCreateEdit):
    data = PatientSerivce.create_patient(payload)
    return {'message': 'Created', 'data': data}

@patient_router.put('/{patient_id}', status_code=200)
def edit_patient(patient_id: int, payload: PatientsCreateEdit):
    data = PatientSerivce.edit_patient(payload)
    return {'message': 'success', 'data': data}

@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
    PatientSerivce.delete_patient(patient_id)
    return {'messge': 'account deleted successfully.'}