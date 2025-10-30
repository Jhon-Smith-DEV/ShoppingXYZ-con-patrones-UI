from .conexion import ContextoDB

class ProductoDAO:
    _contexto = ContextoDB

    @classmethod
    def mostrar(cls):
        try:
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        SELECT p.id, p.nombre, p.descripcion, p.precio, p.categoria_id, c.nombre
                        FROM productos p
                        JOIN categorias c ON p.categoria_id = c.id
                        ORDER BY p.id ASC
                    """)
                    rows = cursor.fetchall()
                    return [
                        {"id": r[0], "nombre": r[1], "descripcion": r[2], "precio": float(r[3]), "categoria_id": r[4], "categoria": r[5]}
                        for r in rows
                    ]
        except Exception as e:
            print(f"Error al listar productos: {e}")
            return []

    @classmethod
    def insertar(cls, dic):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO productos (nombre, descripcion, precio, categoria_id) VALUES ({s}, {s}, {s}, {s})",
                        (dic.get('nombre'), dic.get('descripcion'), dic.get('precio'), dic.get('categoria_id'))
                    )
                conn.commit()
        except Exception as e:
            print(f"Error al insertar producto: {e}")

    @classmethod
    def obtener(cls, id):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT id, nombre, descripcion, precio, categoria_id FROM productos WHERE id = {s}", (id,))
                    r = cursor.fetchone()
                    if r:
                        return {"id": r[0], "nombre": r[1], "descripcion": r[2], "precio": float(r[3]), "categoria_id": r[4]}
            return None
        except Exception as e:
            print(f"Error al obtener producto: {e}")
            return None

    @classmethod
    def actualizar(cls, dic):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE productos SET nombre = {s}, descripcion = {s}, precio = {s}, categoria_id = {s} WHERE id = {s}",
                        (dic.get('nombre'), dic.get('descripcion'), dic.get('precio'), dic.get('categoria_id'), dic.get('id'))
                    )
                conn.commit()
        except Exception as e:
            print(f"Error al actualizar producto: {e}")

    @classmethod
    def eliminar(cls, id):
        try:
            s = cls._contexto.obtenerParametro()
            with cls._contexto.obtenerConexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"DELETE FROM productos WHERE id = {s}", (id,))
                conn.commit()
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
