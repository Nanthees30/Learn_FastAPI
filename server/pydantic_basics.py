from pydantic import BaseModel, EmailStr

class person(BaseModel):
    id: int
    name: str
    email: EmailStr

valied_data = person(
    id=1,
    name='Bharathi',
    email='bharathi@gmail.com'
    )

print(valied_data)