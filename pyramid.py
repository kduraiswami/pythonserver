
import sys
sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pyramid/__init__.py")

import pyramid
import pdb
pdb.set_trace()

from pyramid.config import Configurator
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