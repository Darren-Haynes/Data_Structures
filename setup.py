from setuptools import setup

setup(
    name='Binary Search Tree',
    description='Create a Binary Search Tree structure',
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
            'bst=bst:main'
        }
    }
)
