from setuptools import setup
import ast
import codecs
import os
import re


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('jinja2_slug/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


def _read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='jinja2-slug',
    version=version,
    description='Jinja2 Extension for creating slugs',
    long_description=_read('README.rst'),
    author='Marvin Steadfast',
    author_email='marvin@xsteadfastx.org',
    maintainer='Marvin Steadfast',
    maintainer_email='marvin@xsteadfastx.org',
    license='MIT',
    url='https://github.com/xsteadfastx/jinja2-slug',
    packages=[
        'jinja2_slug'
    ],
    install_requires=[
        'jinja2',
        'unicode-slugify'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python'
    ],
    keywords=['jinja2', 'extension', 'slug']
)
