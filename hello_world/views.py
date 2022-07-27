from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from hello_world.serializers import data_serializer
from hello_world.services import get_hello_world_data


def hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        content=data_serializer(
            get_hello_world_data()
        ),
        content_type='application/json',
        status=HTTPStatus.OK
    )