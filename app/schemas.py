from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int
    city: str

class StudentUpdate(BaseModel):
    name: str
    age: int
    city: str    

class UserCreate(BaseModel):
    name: str
    email: str
    password: str    
class UserLogin(BaseModel):
    email: str
    password: str
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True    