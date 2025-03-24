from ..services.sum_thread import SumThread

class ThreadFactory:
    def __init__(self, result_manager):
        self.result_manager = result_manager
    
    def create_threads(self, num_threads):
        return [SumThread(f"Hilo-{i+1}", self.result_manager) for i in range(num_threads)]