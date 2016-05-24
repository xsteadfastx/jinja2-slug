from jinja2.ext import Extension
from slugify import slugify


def slug(value):
    return slugify(value, only_ascii=True)


class SlugExtension(Extension):
    def __init__(self, environment):
        super(SlugExtension, self).__init__(environment)
        environment.filters['slug'] = slug
