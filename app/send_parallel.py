import logging
import queue
import threading
import time

import requests

THREADS_COUNT = 25
logging.basicConfig(level=logging.DEBUG)


def send_thread(server, api, result_queue):
    logging.debug(f"Running request to server: {server}{api}")
    link = server + api
    base = exponent = 1
    try:
        result = requests.post(link)
    except Exception as e:
        logging.error(f"An exception was raised! continuing. Exception: {e}")
        result_queue.put("Failed", 500)
        return
    while not result.ok:
        logging.debug(f"Result returned: {result.status_code}")
        sleep_time = base ** exponent
        result = requests.post(link)
        time.sleep(sleep_time)
        base += 1
        exponent += 1
        if sleep_time > 1000:
            logging.error(f"Failed running request to server {server}{api}")
            result_queue.put("Failed", 500)
            return

    result_queue.put(result.text, 201)


def send_to_all_parallel_servers(servers, api):
    logging.debug(f"Running API request {api} to the servers {servers}")
    q = queue.Queue()
    threads = [threading.Thread(target=send_thread, args=(server, api, q)) for server in servers]
    for th in threads:
        th.daemon = True
        th.start()

    return q.get()
