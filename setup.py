"""Setup tools."""
from setuptools import setup

setup(
<<<<<<< HEAD
    name='Insertion Sort',
    description='Insertion sort algorithm',
=======
<<<<<<< HEAD
    name='Bubble Sort',
    description='Bubble sort algorithm',
=======
    name='data-structures',
    description='Data structure written in Python',
>>>>>>> fa0b3a1b2778a018384d6f762a969d0d025c7c4a
>>>>>>> 713c0ddff52ac83cd9eb0aed9f797312b5a708a8
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
<<<<<<< HEAD
            'bubble=bubble:main'
=======
>>>>>>> fa0b3a1b2778a018384d6f762a969d0d025c7c4a
        }
    }
)
