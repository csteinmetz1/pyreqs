from setuptools import setup

setup(
    name = 'pyreqs',
    version = '0.1.0',
    packages = ['pyreqs'],
    install_requires=['stdlib_list'],
    entry_points = {
        'console_scripts': [
            'pyreqs = pyreqs.__main__:main'
        ]
    })