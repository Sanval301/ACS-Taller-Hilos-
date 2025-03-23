from abc import ABC, abstractmethod
from ..models.sequence import Sequence

class SequenceFactory(ABC):
    """Interfaz para el Factory Method de secuencias."""
    
    @abstractmethod
    def create_sequence(self, n1, n2):
        """
        Crea una instancia de secuencia.
        
        Args:
            n1 (int): Número inicial
            n2 (int): Número final
            
        Returns:
            Sequence: Una instancia de secuencia
        """
        pass

class BasicSequenceFactory(SequenceFactory):
    """Factory Method concreto para secuencias básicas."""
    
    def create_sequence(self, n1, n2):
        """
        Crea una instancia de secuencia básica.
        
        Args:
            n1 (int): Número inicial
            n2 (int): Número final
            
        Returns:
            Sequence: Una instancia de Sequence
        """
        return Sequence(n1, n2)
