from setuptools import setup, find_packages

version = '0.1.1'

setup(
    name='posts',
    version=version,
    description='A Python library for send mail easily',

    long_description=open('README.rst').read(),
    keyword='email mail python',
    author='Jiaju.Chen',
    author_email='jiaju.chen@ele.me',
    url='https://github.com/importcjj/Post',

    lisence='BSD2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
