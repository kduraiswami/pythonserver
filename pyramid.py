import sys
import os
import inspect

import pdb
pdb.set_trace()

from pyramid.config import Configurator
from pyramid import __package__
from pyramid.response import Response


def hello_world(request):
    return Response(
        'Hello Pyramid!\n',
        content_type='text/plain',
    )

config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()