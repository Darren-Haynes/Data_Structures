"""Setup tools."""
from setuptools import setup

setup(
    name='data-structures',
    description='Data structure written in Python',
    package_dir={'': 'src'},
    author='Darren Haynes',
    author_email='dummy-email@zoho.com',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox', 'faker'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
        }
    }
)
