ERROR_TYPE_FIELDS_VALIDATION = "FIELDS_VALIDATION_ERROR"
ERROR_TYPE_MISC = "MISC_ERROR"


def api_error_resource_does_not_exist():
    content = {}
    content['status'] = 400
    content['error'] = {
        'error': ERROR_TYPE_MISC,
        'description': "Resource does not exist."
    }
    return content, 400


def api_misc_error(message, code=400):
    content = {}
    content['status'] = code
    content['error'] = {
        'error': ERROR_TYPE_MISC,
        'description': message
    }
    return content, code


def validation_error(field_errors):
    code = 422
    content = {}
    content['status'] = code
    content['error'] = {
        'error': ERROR_TYPE_FIELDS_VALIDATION,
        'description': "One or more fields raised validation errors.",
        'fields': field_errors
    }
    return content, code


def api_response(code, data=None, error=None, header=None):
    content = {'status': code}
    if data is not None:
        content['data'] = data
    if error is not None:
        content['error'] = error
    if header is not None:
        return content, code, header
    return content, code


def api_response_no_input():
    return api_response(400, error="No input data provided")
