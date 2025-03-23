import logging

def setup_logger():
    """Configura y retorna un logger para la aplicación."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger('sequence_calculator')
