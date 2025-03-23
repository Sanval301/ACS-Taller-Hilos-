from abc import ABC, abstractmethod

class Subject(ABC):
    """Interface del Sujeto para el patrón Observer."""
    
    @abstractmethod
    def register_observer(self, observer):
        """Registra un observador."""
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        """Elimina un observador."""
        pass
    
    @abstractmethod
    def notify_observers(self):
        """Notifica a todos los observadores."""
        pass

class Observer(ABC):
    """Interface del Observador para el patrón Observer."""
    
    @abstractmethod
    def update(self, subject):
        """
        Actualiza al observador con información del sujeto.
        
        Args:
            subject: El sujeto que notifica el cambio
        """
        pass

class SequenceSubject(Subject):
    """Implementación concreta del Sujeto para la secuencia."""
    
    def __init__(self):
        self.observers = []
        self.sequence = None
        
    def register_observer(self, observer):
        """Registra un observador."""
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer):
        """Elimina un observador."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self):
        """Notifica a todos los observadores."""
        for observer in self.observers:
            observer.update(self)
    
    def set_sequence(self, sequence):
        """
        Establece la secuencia y notifica a los observadores.
        
        Args:
            sequence (list): Secuencia calculada
        """
        self.sequence = sequence
        self.notify_observers()
