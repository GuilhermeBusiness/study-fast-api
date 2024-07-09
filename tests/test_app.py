from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'username',
            'password': '1234',
            'email': 'user@example.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'username',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'username', 'email': 'user@example.com'}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'gostoso',
            'password': '1234',
            'email': 'gostoso@example.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'gostoso',
        'email': 'gostoso@example.com',
        'id': 1,
    }


def test_delete_user(client):

    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
