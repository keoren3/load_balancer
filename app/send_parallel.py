import queue
import threading
import time

import requests

THREADS_COUNT = 25


def send_thread(server, result_queue):
    base = exponent = 1
    result = requests.post(server)
    while not result.ok:
        result = requests.post(server)
        time.sleep(base ** exponent)
        base += 1
        exponent += 1

    result_queue.put({server: result.text})


def send_to_all_parallel_servers(servers):
    q = queue.Queue()
    threads = [threading.Thread(target=send_thread, args=(server, q)) for server in servers]
    for th in threads:
        th.daemon = True
        th.start()

    return q.get()
