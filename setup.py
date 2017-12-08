from setuptools import setup

setup(
    name='Bubble Sort',
    description='Bubble sort algorithm',
    package_dir={'': 'src'},
    author='Darren Haynes',
    author_email='dummy-email@zoho.com',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
            'bubble=bubble:main'
        }
    }
)
