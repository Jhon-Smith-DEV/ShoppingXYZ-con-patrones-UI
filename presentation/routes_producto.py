from flask import Blueprint, render_template, request, redirect, url_for
from business.producto_service import ProductoService

producto_bp = Blueprint('producto', __name__, template_folder='../templates')

@producto_bp.route('/')
def listar():
    productos = ProductoService.listar()
    return render_template('productos/listar.html', productos=productos)

@producto_bp.route('/crear', methods=['GET','POST'])
def crear():
    categorias = ProductoService.categorias()
    if request.method == 'POST':
        ProductoService.crear({
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': request.form.get('precio'),
            'categoria_id': request.form.get('categoria_id')
        })
        return redirect(url_for('producto.listar'))
    return render_template('productos/form.html', categorias=categorias, accion='Crear')

@producto_bp.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    producto = ProductoService.obtener(id)
    categorias = ProductoService.categorias()
    if request.method == 'POST':
        ProductoService.actualizar({
            'id': id,
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': request.form.get('precio'),
            'categoria_id': request.form.get('categoria_id')
        })
        return redirect(url_for('producto.listar'))
    return render_template('productos/form.html', producto=producto, categorias=categorias, accion='Editar')

@producto_bp.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoService.eliminar(id)
    return redirect(url_for('producto.listar'))
