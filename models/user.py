from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta
users = Table(
  'users',meta,
  Column('id',Integer),
  Column('first_name',String(100)),
  Column('last_name',String(100)),
  Column('email',String(100)),
  Column('mobile',Integer),
  Column('location',String(100))
)