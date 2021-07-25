import os

user = "test"
password = "password"
host = "localhost"
port = 5432
database = "fakedb"

# # the right way to do it
# user = os.environ.get('POSTGRES_USER')
# password = os.environ.get('POSTGRES_PASSWORD')
# host = os.environ.get('POSTGRES_HOST')
# database = os.environ.get('POSTGRES_DB')
# port = os.environ.get('POSTGRES_PORT')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
# print(f'first DATABASE_CONNECTION_URI {DATABASE_CONNECTION_URI}')
 