import json
from server.models import User


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode())


def test_get_users(test_client, init_database):
    response = test_client.get('/api/users')
    assert response.status_code == 200


def test_create_user(test_client, init_database):
    request_content = {
        'name': "Test User",
        'status': 1
    }
    response = test_client.post('/api/users',
                                data=json.dumps(request_content),
                                content_type='application/json')
    assert response.status_code == 204
    assert len(User.query.all()) == 1
