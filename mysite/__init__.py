from pyramid.config import Configurator
import views


def main(globlal_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('hello_world', '/hello')
    config.add_route('home_page', '/')
    config.add_route('my_world', '/world')
    config.add_route('list', '/list')
    config.add_route('add', '/list/add')
    config.add_route('view', '/list/{id}')
    config.add_route('edit', '/list/{id}/edit')
    config.add_route('delete', '/list/{id}/delete')
    config.scan()
    return config.make_wsgi_app()