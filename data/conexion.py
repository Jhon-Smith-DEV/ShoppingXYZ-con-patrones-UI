import os
import psycopg2

class ContextoDB:
    @staticmethod
    def obtenerParametro():
        return "%s"

    @staticmethod
    def obtenerConexion():
        db_host = os.environ.get('DATABASE_HOST', 'localhost')
        db_port = os.environ.get('DATABASE_PORT', '5432')
        db_name = os.environ.get('DATABASE_NAME', 'flask_db')
        db_user = os.environ.get('DATABASE_USER', 'flask_user')
        db_pass = os.environ.get('DATABASE_PASSWORD', 'flask_pass')
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        return conn
