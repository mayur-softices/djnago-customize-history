from setuptools import setup, find_packages

setup(
    name='django-customized-history',
    version='1.0.0',
    license='MIT',
    author="Mayur Ariwala",
    author_email='mayur@softices.com',
    packages=find_packages('django_customize_history'),
    url='https://github.com/mayur-softices/djnago-customize-history/',
    keywords='Django Customize History',
    install_requires=[
        'django',
    ],
)
