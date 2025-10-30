from data.categoria_dao import CategoriaDAO

class CategoriaService:
    @staticmethod
    def listar():
        return CategoriaDAO.mostrar()

    @staticmethod
    def obtener(id):
        return CategoriaDAO.obtener(id)

    @staticmethod
    def crear(dic):
        return CategoriaDAO.insertar(dic)

    @staticmethod
    def actualizar(dic):
        return CategoriaDAO.actualizar(dic)

    @staticmethod
    def eliminar(id):
        return CategoriaDAO.eliminar(id)


if __name__ == '__main__':
    print('--- Categoria Service Test ---')
    print('Listar:', CategoriaService.listar())
    # CategoriaService.crear({'nombre':'Prueba Cat', 'descripcion':'desc prueba'})
    # print('Después crear:', CategoriaService.listar())
    # cats = CategoriaService.listar()
    # if cats:
    #     cid = cats[0]['id']
    #     print('Obtener:', CategoriaService.obtener(cid))
    #     CategoriaService.actualizar({'id': cid, 'nombre': 'Actualizada', 'descripcion': 'actualizada desc'})
    #     print('Después actualizar:', CategoriaService.obtener(cid))
    #     CategoriaService.eliminar(cid)
    #     print('Después eliminar:', CategoriaService.listar())
    # else:
    #     print('No hay categorías para probar.')
