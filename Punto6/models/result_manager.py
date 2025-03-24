import threading

class ResultManager:
    def __init__(self):
        self.results = {}
        self.lock = threading.Lock()
    
    def store_result(self, thread_name, result):
        with self.lock:
            self.results[thread_name] = result
    
    def get_winner(self):
        with self.lock:
            return max(self.results.items(), key=lambda x: x[1])