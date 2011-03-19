# -*- coding: utf-8 -*-

from elixir import *
from datetime import *
import os

metadata.bind = "sqlite:///ziluolan.sqlitedb"
metadata.bind.echo = True

class Product(Entity):
    sn = Field(String(30))
    price = Field(Float)
    brand = Field(Unicode(30))

class Cart(Entity):
    sn = Field(String(30))
    price = Field(Integer)
    number = Field(Integer)
    
class Archive(Entity):
    sn = Field(String(30))
    date = Field(DateTime, default=datetime.now)
    price = Field(Float)
    number = Field(Integer)

print("init")
setup_all()
if not os.path.exists('ziluolan.sqlitedb'):
    create_all()
    
