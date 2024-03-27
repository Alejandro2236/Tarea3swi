import codecs
import csv
import json
import os

from estudiantes.estudiante import Estudiante


class ControladorEstudiantes:
    def __init__(self):
        self._estudiantes: list[Estudiante] = []

    def cargar_estudiantes_desde_csv(self, ruta_archivo_csv) -> bool:
        try:
            with codecs.open(ruta_archivo_csv, 'r', encoding='utf-8-sig') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    id_estudiante, nombre, apellido = fila
                    estudiante = Estudiante(id_estudiante, nombre, apellido)
                    self._estudiantes.append(estudiante)
            self.guardar_estudiantes_en_json(ruta_archivo_csv)
            return True
        except FileNotFoundError:
            print(f'Archivo csv no encontrado en {ruta_archivo_csv}')
            return False

    def guardar_estudiantes_en_json(self, ruta_archivo_csv) -> bool:
        ruta_archivo_json = os.path.splitext(ruta_archivo_csv)[0] + '.json'
        estudiantes_json = [estudiante.to_dict() for estudiante in self._estudiantes]
        with open(ruta_archivo_json, 'w', encoding='utf-8') as archivo_json:
            json.dump(estudiantes_json, archivo_json, indent=4, ensure_ascii=False)
        return True
