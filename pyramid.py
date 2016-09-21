import pdb
import importlib.util

ConfigSpec = importlib.util.spec_from_file_location("pyramid.config", "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pyramid/config/__init__.py")
Config = importlib.util.module_from_spec(ConfigSpec)
ConfigSpec.loader.exec_module(Config)

ResponseSpec = importlib.util.spec_from_file_location("pyramid.response", "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pyramid/response.py")
Response = importlib.util.module_from_spec(ResponseSpec)
ResponseSpec.loader.exec_module(Response)

def hello_world(request):
    return ResponseSpec.Response(
        'Hello Pyramid!\n',
        content_type='text/plain',
    )

Configurator = Config.Configurator()
Configurator.add_route('hello', '/hello')
Configurator.add_view(hello_world, route_name='hello')
app = Configurator.make_wsgi_app()