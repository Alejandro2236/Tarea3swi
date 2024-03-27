from estudiantes.controlador_estudiantes import ControladorEstudiantes


def main():
    controlador = ControladorEstudiantes()
    ruta_csv = input("Ingrese la ruta del archivo CSV de estudiantes: ")
    controlador.cargar_estudiantes_desde_csv(ruta_csv)


if __name__ == '__main__':
    main()
