# -*- coding: utf-8 -*-

from elixir import *
from datetime import *

metadata.bind = "sqlite:///ziluolan.sqlitedb"
metadata.bind.echo = True

class Brand(Entity):
    sn = Field(String(30))
    name = Field(Unicode(30))

class Product(Entity):
    sn = Field(String(30))
    price = Field(Float)
    brand_id = Field(Integer)
    
class Cart(Entity):
    sn = Field(String(30))
    status = Field(Integer)
    product_id = Field(Integer)
    
class Archive(Entity):
    sn = Field(String(30))
    date = Field(DateTime, default=datetime.now)
    cart_id = Field(Integer)
    
import os

if __name__ == '__main__':
    setup_all()
    if not os.path.exists('ziluolan.sqlitedb'):
        create_all()
    
    #query
    brand = Brand.query.first()
    if brand is None:
        Brand(sn="ZL", name=u"紫罗兰")
        #insert
    else:
        if brand.sn != "ZLL":
            #update
            brand.sn = "ZLL"
        else:
            #delete
            brand.delete()
    
    session.commit()