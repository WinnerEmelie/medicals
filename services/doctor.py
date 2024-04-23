from fastapi import HTTPException

from schema.doctor import DoctorsCreate, Doctors, doctors
from schema.patient import Patients, patients
from utils.doctor import DoctorHelpers

class DoctorService:

    @staticmethod
    def create_doctor(payload: DoctorsCreate):
        id =(doctors)
        patient: Patients = patients[payload.patient]
        doctor = Doctors (

            id: int, 
            name= str
            specialization= str
            phone= str
        )
    
    @staticmethod
    def get_doctor_by_id(doctor_id: int):
        doctor = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(detail='Flight not found', status_code=404)
        return doctor
    
    @staticmethod
    def edit_doctor(doctor_id: int, payload: DoctorsCreate):
        doctor: Doctors  = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=404)
        patient: Patients = patients[payload.patient]
    
    @staticmethod
    def delete_doctor(doctor_id):
        doctor: Doctors  = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=404)
        del doctors[doctor_id]