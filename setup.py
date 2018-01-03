import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="advanced_python",
    version="0.0.1",
    author="Marko Esna",
    author_email="maesna@ttu.ee",
    description="Tool to extract information about bitcoin price.",
    license="MIT",
    url="https://github.com/mesna/advanced-python",
    packages=['advanced_python', 'tests'],
    long_description=read('README'),
    zip_safe=False
)
