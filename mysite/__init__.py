from pyramid.config import Configurator
import app


def main(globlal_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('hello_world', '/hello')
    config.add_route('home_page', '/')
    config.add_route('my_world', '/world')
    config.scan()
    return config.make_wsgi_app()