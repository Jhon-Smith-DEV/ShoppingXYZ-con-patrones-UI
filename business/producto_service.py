from data.producto_dao import ProductoDAO
from data.categoria_dao import CategoriaDAO

class ProductoService:
    @staticmethod
    def listar():
        return ProductoDAO.mostrar()

    @staticmethod
    def obtener(id):
        return ProductoDAO.obtener(id)

    @staticmethod
    def crear(dic):
        return ProductoDAO.insertar(dic)

    @staticmethod
    def actualizar(dic):
        return ProductoDAO.actualizar(dic)

    @staticmethod
    def eliminar(id):
        return ProductoDAO.eliminar(id)

    @staticmethod
    def categorias():
        return CategoriaDAO.mostrar()


if __name__ == '__main__':
    print('--- Producto Service Test ---')
    print('Listar productos:', ProductoService.listar())
    print('Listar categorias:', ProductoService.categorias())
    cats = ProductoService.categorias()
    if not cats:
        from data.categoria_dao import CategoriaDAO
        CategoriaDAO.insertar({'nombre':'CatPrueba','descripcion':'desc'})
        cats = ProductoService.categorias()
    cid = cats[0]['id'] if cats else None
    if cid:
        ProductoService.crear({'nombre':'ProdPrueba','descripcion':'desc prod','precio':9.99,'categoria_id':cid})
        print('Después crear:', ProductoService.listar())
        prods = ProductoService.listar()
        if prods:
            pid = prods[0]['id']
            print('Obtener:', ProductoService.obtener(pid))
            ProductoService.actualizar({'id': pid, 'nombre':'ProdUpd','descripcion':'upd','precio':5.55,'categoria_id':cid})
            print('Después actualizar:', ProductoService.obtener(pid))
            ProductoService.eliminar(pid)
            print('Después eliminar:', ProductoService.listar())
    else:
        print('No hay categorías para probar productos.')
