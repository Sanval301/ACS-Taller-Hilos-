import threading

class SharedList:
    """
    Implementación de una lista compartida utilizando el patrón Singleton.
    Proporciona acceso seguro a la lista desde múltiples hilos.
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SharedList, cls).__new__(cls)
                cls._instance.data = []
                cls._instance.data_lock = threading.Lock()
                cls._instance.observers = []
                cls._instance.running = True
        return cls._instance
    
    def add_value(self, value):
        """Añade un valor a la lista de manera segura con un bloqueo."""
        with self.data_lock:
            self.data.append(value)
    
    def get_values(self):
        """Retorna una copia de la lista actual para evitar modificaciones directas."""
        with self.data_lock:
            return self.data.copy()
    
    def update_value(self, index, value):
        """Actualiza un valor específico en la lista de manera segura."""
        with self.data_lock:
            if 0 <= index < len(self.data):
                self.data[index] = value
    
    def get_sum(self):
        """Calcula la suma de todos los elementos en la lista."""
        with self.data_lock:
            return sum(self.data)
    
    def get_length(self):
        """Retorna la longitud actual de la lista."""
        with self.data_lock:
            return len(self.data)
    
    # Métodos para el patrón Observer
    def register_observer(self, observer):
        """Registra un observador para ser notificado."""
        self.observers.append(observer)
    
    def notify_stop(self):
        """Notifica a todos los observadores que deben detenerse."""
        self.running = False
        for observer in self.observers:
            observer.stop()
    
    def should_continue(self):
        """Indica si los hilos deben continuar ejecutándose."""
        return self.running