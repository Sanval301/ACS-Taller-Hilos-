import logging
import time

class Logger:
    """Gestor de logs para la aplicación."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # Configurar el logger
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.StreamHandler()
                ]
            )
            cls._instance.logger = logging.getLogger('ThreadProject')
        return cls._instance
    
    def info(self, message):
        """Registra un mensaje informativo."""
        self.logger.info(message)
    
    def warning(self, message):
        """Registra un mensaje de advertencia."""
        self.logger.warning(message)
    
    def error(self, message):
        """Registra un mensaje de error."""
        self.logger.error(message)
    
    def debug(self, message):
        """Registra un mensaje de depuración."""
        self.logger.debug(message)
