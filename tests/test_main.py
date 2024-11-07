from http import HTTPStatus as status


def test_read_root_retorna_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == status.OK  # Garanta que o status code é 200
    assert response.json() == {
        'message': 'Hello, World!'
    }  # Garanta que a resposta é a esperada


def test_create_user_retorna_created_e_usuario(client):
    response = client.post(
        '/create_user/',
        json={'name': 'John Doe', 'email': 'john@email.com', 'password': '123'},
    )

    assert response.status_code == status.CREATED  # Garanta que o status code é 201
    assert response.json() == {'id': 1, 'name': 'John Doe', 'email': 'john@email.com'}


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == status.OK
    # Garanta que a resposta é a esperada
    assert response.json() == {
        'users': [{'id': 1, 'name': 'John Doe', 'email': 'john@email.com'}]
    }


def test_update_user(client):
    response = client.put(
        '/update_user/1',
        json={'name': 'Claudio', 'email': 'claudio@email.com', 'password': '123'},
    )

    assert response.status_code == status.OK
    assert response.json() == {'id': 1, 'name': 'Claudio', 'email': 'claudio@email.com'}


def test_update_user_not_fount(client):
    response = client.put(
        '/update_user/2',
        json={'name': 'Claudio', 'email': 'claudio@gmail.com', 'password': '123'},
    )

    assert response.status_code == status.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/delete_user/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/delete_user/2')

    assert response.status_code == status.NOT_FOUND
