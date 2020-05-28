import os
"""
File for placement server constants.
Can not depend on any other file in this project only python built ins

"""
SERVER_PERMISSION_GROUPS = ['admin', 'alpha', 'beta']

BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CODE_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'replays')
UPLOAD_RATE_LIMIT_MINUTES = 4.5  # TODO: Make use of this.

# Server names (Should be exactly as the services defined in docker-compose file)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
POSTGRES_HOST= os.getenv("POSTGRES_HOST","localhost")

# Server ports
REDIS_PORT= os.getenv('REDIS_PORT', "6379")
POSTGRES_PORT= os.getenv("POSTGRES_PORT","5432")

# Users 
POSTGRES_USER= os.getenv("POSTGRES_USER","postgres")

# Password (Only used in development environment, defaults to OS env)
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","postgres")

# Databases
POSTGRES_DB= os.getenv("POSTGRES_DB","saltie")