from os import path

import logic.app.utils.archivos_util as archivos_util
from logic.app.configs.variables import Variable
from logic.app.models.modelos import Archivo
from logic.libs.variables.variables import dame


def crear(a: Archivo):
    """
    Crea un archivo en el sistema de archivos
    """
    archivos_util.crear(obtener_directorio_absoluto(a), a.nombre, a.contenido)


def borrar(a: Archivo):
    """
    Borra un archivo en el sistema de archivos
    """
    archivos_util.borrar(obtener_directorio_absoluto(a), a.nombre)


def obtener(a: Archivo) -> bytes:
    """
    Obtiene un archivo de la base de datos y del sistema de archivos
    """
    return archivos_util.obtener(obtener_directorio_absoluto(a), a.nombre)


def obtener_directorio_absoluto(a: Archivo) -> str:
    """
    Obtiene el directorio absoluto en donde esta guardado el archivo en el sistema de archivos
    """
    dir_base = dame(Variable.DIRECTORIO_SISTEMA_ARCHIVOS)
    return path.join(dir_base, obtener_directorio_relativo(a))


def obtener_directorio_relativo(a: Archivo) -> str:
    """
    Obtiene el directorio relativo en donde esta guardado el archivo en el sistema de archivos
    """
    return path.join(str(a.tipo.value).lower(), str(a.id_modelo))