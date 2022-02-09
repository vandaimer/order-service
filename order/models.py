from sqlalchemy import Column, Integer, String, Table, Float, DateTime

from order.db import metadata


Orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', String),
    Column('product_code', String),
    Column('customer_fullname', String),
    Column('product_name', String),
    Column('total_amount', Float),
    Column('created_at', DateTime)
)
