from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Jane Doe"


user = User(id="123")


print(user, user.name, user.id, type(user.__class__))


print(user.dict())
print(user.model_dump())
print(user.model_dump_json())


print(User.dict())