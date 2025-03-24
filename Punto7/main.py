import psutil
import os

def list_processes():
    print("PID\tNombre")
    for process in psutil.process_iter(attrs=['pid', 'name']):
        print(f"{process.info['pid']}\t{process.info['name']}")

def kill_process(pid):
    try:
        os.kill(pid, 9)
        print(f"Proceso {pid} terminado con éxito.")
    except ProcessLookupError:
        print(f"No se encontró el proceso con PID {pid}.")
    except PermissionError:
        print(f"No tienes permisos para terminar el proceso {pid}.")
    except Exception as e:
        print(f"Error al intentar terminar el proceso {pid}: {e}")

def main():
    list_processes()
    try:
        pid = int(input("Ingrese el PID del proceso a terminar: "))
        kill_process(pid)
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
