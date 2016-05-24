===========
Jinja2 Slug
===========

Jinja2 Extenson for creating slugs. It can be used to create URLs. It uses the `unicode-slugify`_ module.

.. _`unicode-slugify`: https://github.com/mozilla/unicode-slugify


Installation
------------

**jinja2-slug** is available for download from `PyPI`_ via `pip`_::

    $ pip install jinja2-slug

.. _`PyPI`: https://pypi.python.org/pypi
.. _`pip`: https://pypi.python.org/pypi/pip/


Usage
-----

.. code-block:: python

   from jinja2 import Environment


   env = Environment(extensions=['jinja2_slug.SlugExtension'])

   template = env.from_strong('This is a test')

   template.render()
