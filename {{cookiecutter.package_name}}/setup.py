import setuptools

setuptools.setup(

    name='{{ cookiecutter.package_name }}',
    version='{{ cookiecutter.package_version }}',
    url='{{ cookiecutter.package_url }}',

    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',

    description='{{ cookiecutter.package_description }}',
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    entry_points={
        'console_scripts': [
            ('{{cookiecutter.package_name}} = '
             '{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}:main'),
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
