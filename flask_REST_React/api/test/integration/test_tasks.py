import json
from server.models import Task, User
from server.extensions import db


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode())


def test_create_tasks(test_client, init_database):
    request_content = {
        'name': "test_task",
        'status': 1
    }
    response = test_client.post('/api/tasks',
                                data=json.dumps(request_content),
                                content_type='application/json')
    assert response.status_code == 204
    assert len(Task.query.all()) == 1


def test_get_task(test_client, init_database):

    # get task id
    task = Task.query.first()
    assert task is not None

    response = test_client.get('/api/tasks/' + str(task.id))
    assert response.status_code == 200

    content = json_of_response(response)
    t = content['data']
    assert t['name'] == "test_task"
    assert t['status'] == 1


def test_get_tasks(test_client, init_database):
    response = test_client.get('/api/tasks')
    assert response.status_code == 200

    content = json_of_response(response)
    assert len(content['data']) == 1


def test_update_task(test_client, init_database):
    s = db.session

    # create users
    users = []
    for i in range(1, 5):
        users.append(User(name="user_{}".format(i)))

    s.bulk_save_objects(users)
    user_ids = [id for (id,) in s.query(User.id).all()]
    assert (len(user_ids) == 4)

    task = Task.query.first()
    assert task is not None

    request_content = {
        'name': "test_task_updated",
        'status': 2,
        'users': user_ids,
    }

    response = test_client.patch('/api/tasks/' + str(task.id),
                                 data=json.dumps(request_content),
                                 content_type='application/json'
                                 )
    assert response.status_code == 200

    updated_task = s.query(Task).filter_by(id=task.id).first()

    assert updated_task is not None
    assert updated_task.name == request_content['name']
    assert updated_task.status == request_content['status']
    assert len(updated_task.users) == 4


def test_delete_task(test_client, init_database):
    task = Task.query.first()
    assert task is not None
    response = test_client.delete('/api/tasks/' + str(task.id))
    assert response.status_code == 204
    assert db.session.query(Task.id == task.id).first() is None

