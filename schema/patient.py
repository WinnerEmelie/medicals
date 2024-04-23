from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: int
    height: float
    phone: str

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: float
    phone: str


patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='patient 0', age=30, sex='male', weight='70kg', height='250.5cm', phone='0901'
    ),
    1: Patients(
        id=1, name='patient 1', age=35, sex='female', weight='80kg', height='150.0cm', phone='0801'
    ),
    2: Patients(
        id=2, name='patient 2', age=20, sex='male',weight='75kg', height='200.5cm', phone='0802'
    )
}