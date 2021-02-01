import queue
import threading
import time

import requests

THREADS_COUNT = 25


def send_thread(server, api, result_queue):
    link = server + api
    base = exponent = 1
    result = requests.post(link)
    while not result.ok:
        result = requests.post(link)
        time.sleep(base ** exponent)
        base += 1
        exponent += 1

    result_queue.put({server: result.text})


def send_to_all_parallel_servers(servers, api):
    q = queue.Queue()
    threads = [threading.Thread(target=send_thread, args=(server, api, q)) for server in servers]
    for th in threads:
        th.daemon = True
        th.start()

    return q.get()
