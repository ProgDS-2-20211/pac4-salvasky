import time

def timing_call(function):
    start_time = time.time()
    call = function
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time

