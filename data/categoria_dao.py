from .conexion import ContextoDB

class CategoriaDAO:
    _contexto = ContextoDB

    @classmethod
    def mostrar(cls):
        try:
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT id, nombre, descripcion FROM categorias ORDER BY id ASC")
                    rows = cursor.fetchall()
                    return [{"id": r[0], "nombre": r[1], "descripcion": r[2]} for r in rows]
        except Exception as e:
            print(f"Error al listar categorias: {e}")
            return []

    @classmethod
    def insertar(cls, dic):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"INSERT INTO categorias (nombre, descripcion) VALUES ({s}, {s})", (dic.get('nombre'), dic.get('descripcion')))
                conn.commit()
        except Exception as e:
            print(f"Error al insertar categoria: {e}")

    @classmethod
    def obtener(cls, id):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT id, nombre, descripcion FROM categorias WHERE id = {s}", (id,))
                    r = cursor.fetchone()
                    if r:
                        return {"id": r[0], "nombre": r[1], "descripcion": r[2]}
            return None
        except Exception as e:
            print(f"Error al obtener categoria: {e}")
            return None

    @classmethod
    def actualizar(cls, dic):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"UPDATE categorias SET nombre = {s}, descripcion = {s} WHERE id = {s}",
                                   (dic.get('nombre'), dic.get('descripcion'), dic.get('id')))
                conn.commit()
        except Exception as e:
            print(f"Error al actualizar categoria: {e}")

    @classmethod
    def eliminar(cls, id):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"DELETE FROM categorias WHERE id = {s}", (id,))
                conn.commit()
        except Exception as e:
            print(f"Error al eliminar categoria: {e}")
