from server.extensions import db, ma
from sqlalchemy.ext.hybrid import hybrid_property


task_users = db.Table('task_users',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, status=None):
        self.name = name
        if status:
            self.status = status


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    # Relationships
    users = db.relationship(
        'User',
        secondary=task_users,
        backref=db.backref('tasks')
    )

    @hybrid_property
    def nr_users(self):
        return len(self.annotations)

    def update_users(self, user_ids):
        new_users = db.session.query(User).filter(User.id.in_(user_ids)).all()
        self.users = new_users
        db.session.commit()

    def __init__(self, name, status=0):
        self.name = name
        self.status = status
