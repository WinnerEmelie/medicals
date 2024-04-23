from fastapi import HTTPException

from schema.doctor import DoctorsCreate, Doctors, doctors
from schema.patient import Patients, patients

class AppointmentService:

    @staticmethod
    def create_appointment (payload: AppointmentCreates)
    
        id = int
        patient: Patients = patients[payload.patient]
        doctor: Doctors = Doctors[doctor](
 
            id= int
            name= str
            specialization= str
            phone= str
        )
    
    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        if not appointment_id:
            raise HTTPException(detail='Appointment not found', status_code=404)
        return AppointmentService
    
    @staticmethod
    def update_appointment(appointment_id: int, Appointment):
        appointment: AppointmentService 
        if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
        patient: Patients = patients[patient]

    
    @staticmethod
    def delete_appointment(appointment_id):
        appointment: AppointmentService
        if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
        del appointment [appointment_id]