from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config


@view_config(route_name='hello_world', renderer='templates/hello.jinja2')
def hello(request):
    return dict(name="World we are great")


@view_config(route_name='home_page', renderer='templates/home.jinja2')
def home(request):
    return dict(site_name='Beanfield MettroConnect')


@view_config(route_name='list', renderer='templates/list.jinja2')
def listing(request):
    return dict()


@view_config(route_name='add', renderer='templates/add.jinja2')
def add(request):
    return dict()


@view_config(route_name='view', renderer='templates/view.jinja2')
def view(request):
    return dict()


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit(request):
    return dict()


@view_config(route_name='delete')
def delete(request):
    url = request.route_url('list')
    return HTTPFound(url)


@view_config(route_name='my_world', renderer='templates/world.jinja2', request_param='username')
def world(request):
    name = request.params.get('username')
    return dict(user=name)
