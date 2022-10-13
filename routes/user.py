from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user=APIRouter()
@user.get("/")
async def read_data():
  return conn.execute(users.select()).fetchall()
@user.get("/{id}")
async def read_data(id: int):
  return conn.execute(users.select().where(user.c.id==id)).fetchall()
@user.post("/")
async def write_data(user: User):
  conn.execute(users.insert().values(
    first_name=user.first_name,
    last_name=user.last_name,
    email=user.email,
    mobile=user.mobile,
    location=user.location
  ))
  return conn.execute(users.select()).fetchall()
@user.put("/{id}")
async def update_data(id: int,user: User):
  conn.execute(user.update(
    last_name=user.last_name,
    email=user.email,
    password=user.password
  ).where(user.c.id == id))
  return conn.execute(users.select()).fetchall()
@user.delete("/")
async def delete_data():
  conn.execute(users.delete().where(users.c.id == id))
  return conn.execute(users.select()).fetchall()
