import os
from backend.server_constants import REDIS_HOST, REDIS_PORT

enable_utc = True
worker_max_tasks_per_child = 100

broker_url = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
result_backend = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
broker_transport_options = {'fanout_prefix': True}
task_always_eager = False

# errors from a task that uses apply or is eager will pass up exceptions
task_eager_propagates = True