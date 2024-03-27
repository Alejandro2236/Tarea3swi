class Estudiante:
    def __init__(self, id_estudiante: int, nombre: str, apellido: str):
        self._id = id_estudiante
        self._nombre = nombre
        self._apellido = apellido

    def to_dict(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido
        }
