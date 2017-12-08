"""Setup tools."""
from setuptools import setup

setup(
    name='Linked List',
    description='Create a Binary Search Tree structure',
    package_dir={'': 'src'},
    author='Darren Haynes & Kevin Robinson',
    author_email='dummy-email@zoho.com',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
            'linked_list=linked_list:main'
        }
    }
)
