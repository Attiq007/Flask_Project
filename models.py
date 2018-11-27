# coding: utf-8
from sqlalchemy import Column, Float, MetaData, Table, Text

metadata = MetaData()


t_shop = Table(
    'shop', metadata,
    Column('shop', Text, nullable=False),
    Column('brand', Text, nullable=False),
    Column('address', Text, nullable=False),
    Column('latitude', Float(53), nullable=False),
    Column('longitude', Float(53), nullable=False)
)
