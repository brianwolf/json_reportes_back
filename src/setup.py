import sqlite3
from os import path

from apps.configs.logger.logger import obtener_logger
from apps.configs.variables.claves import Variable
from apps.configs.variables.lector import dame

_logger = obtener_logger('setup')


def db_iniciada() -> bool:
    return path.exists(dame(Variable.DB_SQLITE_RUTA))


def iniciar_db():
    '''
    Crea la base de datos de SQLite mediante el script
    '''

    ruta_script = dame(Variable.DB_SQLITE_SCRIPT)
    _logger.info(
        f'iniciar_db() -> Cargando script SQL ubicado en {ruta_script}')

    with open(ruta_script, mode='r') as script_archivo:
        contenido_script = script_archivo.read()

    ruta_db_sqlite = dame(Variable.DB_SQLITE_RUTA)
    _logger.info(
        f'iniciar_db() -> Conectando con la base de datos SQLite ubicado en {ruta_db_sqlite}')
    conn = sqlite3.connect(ruta_db_sqlite)

    c = conn.cursor()
    c.executescript(contenido_script)

    conn.commit()
    conn.close()

    _logger.info(
        f'iniciar_db() -> Terminado')


if __name__ == "__main__":
    iniciar_db()
