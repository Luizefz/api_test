from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from pullebyte_back.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/create_user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/update_user/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    user_with_id = UserDB(id=user_id, **user.model_dump())

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/delete_user/{user_id}', status_code=HTTPStatus.OK, response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    database.pop(user_id - 1)

    return {'message': 'User deleted'}