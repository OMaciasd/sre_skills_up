import os


class Config:
    POSTGRES_USER = 'your_postgres_user'
    POSTGRES_PASSWORD = 'your_postgres_password'
    POSTGRES_DB = 'your_postgres_db'
    POSTGRES_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://username:password@localhost/dbname'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
