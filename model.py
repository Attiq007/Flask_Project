# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Shop(Base):
    __tablename__ = 'shop'

    shop = Column(Text)
    brand = Column(Text)
    address = Column(Text)
    latitude = Column(Float(53))
    longitude = Column(Float(53))
    id = Column(Integer, primary_key=True, server_default=text("nextval('shop_id_seq'::regclass)"))
    brand_id = Column(ForeignKey('brand.id'), index=True, server_default=text("0"))

    brand1 = relationship('Brand')
