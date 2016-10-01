from pyramid.view import view_config


@view_config(route_name='hello_world', renderer='hello.jinja2')
def hello(request):
    return dict(name="World we are great")

@view_config(route_name='home_page', renderer='home.jinja2')
def home(request):
    return dict(site_name='Beanfield MettroConnect')

@view_config(route_name='my_world', renderer='world.jinja2', request_param='username')
def world(request):
    name = request.params.get('username')
    return dict(user=name)
