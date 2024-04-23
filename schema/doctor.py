from pydantic import BaseModel

from schema.patient import Patients, patients

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    

class DoctorsCreate(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    

doctors: dict[int, Doctors] = {
    0: Doctors(
        id=0, name= 'Dr John', specialization= 'Dentist', phone='0901'    
    ),
    1: Doctors(
        id=1, name= 'Dr Chris', specialization= 'Surgeon', phone='0801',
    ) 
}