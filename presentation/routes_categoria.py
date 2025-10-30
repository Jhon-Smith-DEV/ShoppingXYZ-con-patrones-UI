from flask import Blueprint, render_template, request, redirect, url_for
from business.categoria_service import CategoriaService

categoria_bp = Blueprint('categoria', __name__, template_folder='../templates')

@categoria_bp.route('/')
def listar():
    categorias = CategoriaService.listar()
    return render_template('categorias/listar.html', categorias=categorias)

@categoria_bp.route('/crear', methods=['GET','POST'])
def crear():
    errores = {}
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        # Validaciones
        if not nombre:
            errores['nombre'] = 'El nombre es obligatorio.'
        if not descripcion:
            errores['descripcion'] = 'La descripción es obligatoria.'
        if not errores:
            CategoriaService.crear({'nombre': nombre, 'descripcion': descripcion})
            return redirect(url_for('categoria.listar'))
        else:
            return render_template('categorias/form.html', accion='Crear', errores=errores)
    return render_template('categorias/form.html', accion='Crear')

@categoria_bp.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    categoria = CategoriaService.obtener(id)
    errores = {}
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        # Validaciones
        if not nombre:
            errores['nombre'] = 'El nombre es obligatorio.'
        if not descripcion:
            errores['descripcion'] = 'La descripción es obligatoria.'
        if not errores:
            CategoriaService.actualizar({'id': id, 'nombre': nombre, 'descripcion': descripcion})
            return redirect(url_for('categoria.listar'))
        else:
            categoria_data = {
                'id': id,
                'nombre': nombre,
                'descripcion': descripcion
            }
            return render_template('categorias/form.html', categoria=categoria_data, accion='Editar', errores=errores)
    return render_template('categorias/form.html', categoria=categoria, accion='Editar')

@categoria_bp.route('/eliminar/<int:id>')
def eliminar(id):
    CategoriaService.eliminar(id)
    return redirect(url_for('categoria.listar'))
