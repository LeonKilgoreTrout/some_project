from pydantic import BaseModel
from uuid import UUID


__all__ = ['MenuIn', 'MenuOut', 'SubmenuIn', 'SubmenuOut', 'DishIn', 'DishOut']


class MenuIn(BaseModel):
    title: str
    description: str


class MenuOut(BaseModel):
    id: UUID
    title: str
    description: str
    submenus_count: int = 0
    dishes_count: int = 0

    class Config:
        orm_mode = True


class SubmenuIn(BaseModel):
    title: str
    description: str


class SubmenuOut(BaseModel):
    id: UUID
    title: str
    description: str
    dishes_count: int = 0

    class Config:
        orm_mode = True


class DishIn(BaseModel):
    title: str
    description: str
    price: str


class DishOut(BaseModel):
    id: UUID
    title: str
    description: str
    price: str

    class Config:
        orm_mode = True
