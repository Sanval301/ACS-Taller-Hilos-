import threading
from ..utils.observer import SequenceSubject

class SequenceCalculator:
    """Servicio para calcular secuencias en un hilo separado."""
    
    def __init__(self, sequence_factory):
        """
        Inicializa el calculador con una factory de secuencias.
        
        Args:
            sequence_factory: Factory para crear secuencias
        """
        self.sequence_factory = sequence_factory
        self.subject = SequenceSubject()
        
    def calculate_sequence_threaded(self, n1, n2):
        """
        Calcula la secuencia en un hilo separado.
        
        Args:
            n1 (int): Número inicial
            n2 (int): Número final
        """
        thread = threading.Thread(
            target=self._calculate_sequence,
            args=(n1, n2),
            name="SequenceThread"
        )
        thread.start()
        return thread
    
    def _calculate_sequence(self, n1, n2):
        """
        Función objetivo para el hilo que calcula la secuencia.
        
        Args:
            n1 (int): Número inicial
            n2 (int): Número final
        """
        sequence = self.sequence_factory.create_sequence(n1, n2)
        result = sequence.generate_sequence()
        self.subject.set_sequence(result)
    
    def register_observer(self, observer):
        """
        Registra un observador para recibir resultados.
        
        Args:
            observer: Observador a registrar
        """
        self.subject.register_observer(observer)