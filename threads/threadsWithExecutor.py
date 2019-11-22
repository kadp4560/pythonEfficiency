import logging
import threading
import time
import concurrent.futures
import classDFakeDatabase as FakeDatabase

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase.FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for index in range(8):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
    
