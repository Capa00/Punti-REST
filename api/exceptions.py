from rest_framework.exceptions import ValidationError


class APIError(ValidationError):
    error = ''
    message = ''

    def __init__(self, error=None, message=None, *args, **kwargs):
        self.error = error or self.error
        self.message = message or self.message
        super(APIError, self).__init__({'error': self.error, 'message': self.message})


class Http400(APIError):
    status_code = 400
    error = 'bad_request'
    message = 'Bad request'

class FieldDoesNotExist(Http400):
    error = 'field_not_found'

    def __init__(self, model_view_set, fields, *args, **kwargs):
        fields = [fields] if isinstance(fields, str) else fields
        entity = model_view_set.queryset.model.__name__
        self.message = f'{entity} has no {", ".join(fields)} field{"s" if len(fields)>1 else ""}'
        super().__init__(*args, **kwargs)


class ServerError(ValidationError):
    status_code = 500
    error = 'internal_error'
    message = 'Internal Error'
