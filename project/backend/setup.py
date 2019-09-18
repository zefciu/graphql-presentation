from setuptools import setup

setup(
    name='Film database',
    version='0.1',
    description='Example GraphQL application',
    packages=['movie_base'],
    install_requires=[
        'alembic==1.1.0',
        'Flask==1.1.1',
        'Flask-Cors==3.0.8',
        'Flask-GraphQL==2.0.0',
        'graphene==2.1.8',
        'graphene-sqlalchemy==2.2.2',
        'PyYAML==5.1.2',
        'psycopg2-binary',
        'SQLAlchemy==1.3.8',
    ]
)
