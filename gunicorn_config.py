# Gunicorn configuration file for production settings

import multiprocessing

# Server socket 
bind = '0.0.0.0:8000'

# Worker settings
workers = multiprocessing.cpu_count() * 2 + 1  # Recommended: (2 x $num_of_cores) + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
timeout = 30  # Timeout in seconds

# Logging settings
accesslog = '-'  # Log to stdout
errorlog = '-'  # Log to stderr
loglevel = 'info'  # Log level
