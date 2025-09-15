<<<<<<< HEAD
import os
import shutil

# Definimos la clase FolderManager
class FolderManager:
    # Constructor: se ejecuta cuando creamos un objeto
    def __init__(self, base_path):
        self.base_path = base_path  # atributo de instancia
        # Si no existe la carpeta base, la crea
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Carpeta base '{base_path}' creada.")
        else:
            print(f"Carpeta base '{base_path}' ya existe.")

    # Método para crear carpetas dentro de la carpeta base
    def create_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Carpeta '{folder_name}' creada en {self.base_path}")
        else:
            print(f"La carpeta '{folder_name}' ya existe en {self.base_path}")

    # Método para listar todas las carpetas dentro de la carpeta base
    def list_folders(self):
        folders = [f for f in os.listdir(self.base_path)
                   if os.path.isdir(os.path.join(self.base_path, f))]
        print("Carpetas encontradas:", folders)
        return folders

    # Método para eliminar una carpeta (aunque tenga archivos dentro)
    def delete_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)  # elimina incluso si no está vacía
            print(f"Carpeta '{folder_name}' eliminada.")
        else:
            print(f"La carpeta '{folder_name}' no existe.")


# Ejemplo de uso:
if __name__ == "__main__":
    fm = FolderManager("MiCarpetaBase")  # crea la carpeta base

    fm.create_folder("Proyectos")        # crea una subcarpeta
    fm.create_folder("Documentos")       # crea otra subcarpeta
    fm.list_folders()                    # lista carpetas dentro de la base
    fm.delete_folder("Proyectos")        # elimina la carpeta 'Proyectos'
    fm.list_folders()                    # muestra carpetas restantes
=======
import os
import shutil

# Definimos la clase FolderManager
class FolderManager:
    # Constructor: se ejecuta cuando creamos un objeto
    def __init__(self, base_path):
        self.base_path = base_path  # atributo de instancia
        # Si no existe la carpeta base, la crea
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Carpeta base '{base_path}' creada.")
        else:
            print(f"Carpeta base '{base_path}' ya existe.")

    # Método para crear carpetas dentro de la carpeta base
    def create_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Carpeta '{folder_name}' creada en {self.base_path}")
        else:
            print(f"La carpeta '{folder_name}' ya existe en {self.base_path}")

    # Método para listar todas las carpetas dentro de la carpeta base
    def list_folders(self):
        folders = [f for f in os.listdir(self.base_path)
                   if os.path.isdir(os.path.join(self.base_path, f))]
        print("Carpetas encontradas:", folders)
        return folders

    # Método para eliminar una carpeta (aunque tenga archivos dentro)
    def delete_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)  # elimina incluso si no está vacía
            print(f"Carpeta '{folder_name}' eliminada.")
        else:
            print(f"La carpeta '{folder_name}' no existe.")


# Ejemplo de uso:
if __name__ == "__main__":
    fm = FolderManager("MiCarpetaBase")  # crea la carpeta base

    fm.create_folder("Proyectos")        # crea una subcarpeta
    fm.create_folder("Documentos")       # crea otra subcarpeta
    fm.list_folders()                    # lista carpetas dentro de la base
    fm.delete_folder("Proyectos")        # elimina la carpeta 'Proyectos'
    fm.list_folders()                    # muestra carpetas restantes
>>>>>>> fb8ce65d1588c1dd431967cde35fd8cd83012c6a
