class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'myflaskapp'
    db_connection = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}'
    SQLALCHEMY_DATABASE_URI = f'{db_connection}/{MYSQL_DB}'
