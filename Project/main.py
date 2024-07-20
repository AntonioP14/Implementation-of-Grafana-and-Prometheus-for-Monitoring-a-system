from metrics import REQUEST_TIME, init_metrics_server
import time
import random

@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)

if __name__ == '__main__':
    init_metrics_server()
    while True:
        process_request(random.random())
