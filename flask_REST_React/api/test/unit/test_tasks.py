from server.models import Task, User
from server.extensions import db


def generate_users():
    users = []
    for i in range(1, 5):
        users.append(User(name="user_{}".format(i)))
    return users


def test_update_tasks(test_client, init_database):

    s = db.session
    s.bulk_save_objects(generate_users())
    s.commit()

    # get all user ids
    user_ids = [id for (id,) in s.query(User.id).all()]
    assert (len(user_ids) == 4)

    task = Task(name="test_task")
    s.add(task)
    s.commit()

    task.update_users(user_ids)
    assert (len(task.users) == 4)

    # update invalid ids
    partly_invalid = [1337, 1]
    task.update_users(partly_invalid)
    assert (len(task.users) == 1)
