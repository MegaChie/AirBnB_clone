#!/usr/bin/python3
from models.base_model import BaseModel

bm1 = BaseModel()
print(bm1)
bm2 = BaseModel(**bm1.to_dict())
print(bm2)
print(bm1.id == bm2.id)
