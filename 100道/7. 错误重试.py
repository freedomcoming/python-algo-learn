
from functools import wraps
import time

def retry(*,retry_times=3,max_wait_time=5,errors=(Exception,)):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(retry_times):

                try:
                    return fn(*args, **kwargs)
                except errors:
                    time.sleep(max_wait_time)
            return None
        

        return wrapper
    return decorator  