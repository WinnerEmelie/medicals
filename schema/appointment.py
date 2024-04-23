from pydantic import BaseModel

from schema.patient import Patients, patients
from schema.doctor import Doctors, doctors

class Appointments(BaseModel):
    id: int
    patient: str
    doctor: str
    date: str

class AppointmentsCreate(BaseModel):
    id: int
    patient: str
    doctor: str
    date: str


appointments: dict[int, Appointments] = {
    0:Appointments(
        id=1, patient='patient 1',doctor='doctor 1',date='2024-04-21' 
        )       
}
