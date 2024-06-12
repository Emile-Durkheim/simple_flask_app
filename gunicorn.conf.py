# See https://docs.gunicorn.org/en/stable/deploy.html#nginx-configuration
access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

raw_env = [
   'IS_PROD=true'
]