import threading
import random
import logging
from .services.thhread_factory import ThreadFactory
from .models.result_manager import ResultManager
from .utils.logger import setup_logger

def main():
    setup_logger()
    logging.info("Iniciando el programa")
    
    result_manager = ResultManager()
    factory = ThreadFactory(result_manager)
    
    threads = factory.create_threads(10)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    winner = result_manager.get_winner()
    logging.info(f"El ganador es: {winner[0]} con una suma de {winner[1]}")

if __name__ == "__main__":
    main()
