# fastapi_zero/app.py
from http import HTTPStatus

from fastapi import FastAPI

# from fastapi_zero.schemas import Message
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI(
    title='@raphael ',
    version='0.1.0',
    description='Uma API criada para aprender FastAPI',
)

database = []


@app.get(
    '/',
    response_class=HTMLResponse,
    description='Este endpoint, poderá ser alterado no futuro!',
    status_code=200,
    response_description='Sucesso!',
)
def read_root():
    return HTMLResponse


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}
