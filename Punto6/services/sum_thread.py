import threading
import random
import logging

class SumThread(threading.Thread):
    def __init__(self, name, result_manager):
        super().__init__()
        self.name = name
        self.result_manager = result_manager
    
    def run(self):
        total_sum = sum(random.randint(1, 1000) for _ in range(100))
        logging.info(f"({self.name}) Suma total: {total_sum}")
        self.result_manager.store_result(self.name, total_sum)