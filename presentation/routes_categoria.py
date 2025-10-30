from flask import Blueprint, render_template, request, redirect, url_for
from business.categoria_service import CategoriaService

categoria_bp = Blueprint('categoria', __name__, template_folder='../templates')

@categoria_bp.route('/')
def listar():
    categorias = CategoriaService.listar()
    return render_template('categorias/listar.html', categorias=categorias)

@categoria_bp.route('/crear', methods=['GET','POST'])
def crear():
    if request.method == 'POST':
        CategoriaService.crear({'nombre': request.form.get('nombre'), 'descripcion': request.form.get('descripcion')})
        return redirect(url_for('categoria.listar'))
    return render_template('categorias/form.html', accion='Crear')

@categoria_bp.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    categoria = CategoriaService.obtener(id)
    if request.method == 'POST':
        CategoriaService.actualizar({'id': id, 'nombre': request.form.get('nombre'), 'descripcion': request.form.get('descripcion')})
        return redirect(url_for('categoria.listar'))
    return render_template('categorias/form.html', categoria=categoria, accion='Editar')

@categoria_bp.route('/eliminar/<int:id>')
def eliminar(id):
    CategoriaService.eliminar(id)
    return redirect(url_for('categoria.listar'))
