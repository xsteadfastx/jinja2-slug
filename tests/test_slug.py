# -*- coding: utf-8 -*-

import pytest


from jinja2 import Environment


@pytest.fixture
def environment():
    return Environment(extensions=['jinja2_slug.SlugExtension'])


@pytest.mark.parametrize('input,expected', [
    (u'Motörhead Gang', 'motorhead-gang'),
    ('This is a Test', 'this-is-a-test')
])
def test_slug(input, expected, environment):
    template = environment.from_string('{{ ' + '"' + input + '"' + '|slug }}')

    assert template.render() == expected
