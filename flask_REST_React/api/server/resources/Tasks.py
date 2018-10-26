from flask import request
from flask_restful import Resource
from server.models import Task
from server.schemas import TaskSchema
from . import *
from server.extensions import db
from marshmallow import ValidationError

tasks_schema = TaskSchema(many=True)
task_schema = TaskSchema()


def apply_optional_fields(task, fields):

    if 'description' in fields:
        description = fields['description']
        if description:
            task.description = description

    if 'user_ids' in fields:
        new_user_ids = fields['user_ids']
        task.update_users(new_user_ids)


class TaskAPI(Resource):

    def get(self, id):
        task = Task.query.get(id)
        if not task:
            return api_error_resource_does_not_exist()
        return api_response(200, task_schema.dump(task))

    def patch(self, id):
        task = Task.query.get(id)
        if not task:
            return api_error_resource_does_not_exist()

        json_data = request.get_json(force=True)
        if not json_data:
            return api_response_no_input()

        # validate the data
        try:
            fields = task_schema.load(json_data, partial=True)
        except ValidationError as err:
            return validation_error(err.messages)

        if 'name' in fields:
            task.name = fields['name']

        if 'status' in fields:
            task.status = fields['status']

        apply_optional_fields(task, fields)

        db.session.commit()
        return api_response(200, data=task_schema.dump(task))

    def delete(self, id):
        task = Task.query.get(id)
        if not task:
            return api_error_resource_does_not_exist()

        task_json = task_schema.dump(task)
        db.session.delete(task)
        db.session.commit()
        return api_response(204, data=task_json)


class TaskListAPI(Resource):

    def get(self):
        tasks = Task.query.all()
        return api_response(200, data=tasks_schema.dump(tasks))

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return api_response_no_input()
        try:
            fields = task_schema.load(json_data)
        except ValidationError as err:
            return validation_error(err.messages)

        if Task.query.filter_by(name=fields['name']).all():
            return api_misc_error("Task with this name already exists.", code=409)

        task = Task(name=fields['name'], status=fields['status'])
        apply_optional_fields(task, fields)
        db.session.add(task)
        db.session.commit()
        return api_response(204, data=task_schema.dump(task))
