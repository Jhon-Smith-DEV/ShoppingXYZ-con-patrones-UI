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
    errores = {}
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        precio = request.form.get('precio', '').strip()
        categoria_id = request.form.get('categoria_id', '').strip()

        # Validaciones
        if not nombre:
            errores['nombre'] = 'El nombre es obligatorio.'
        if not descripcion:
            errores['descripcion'] = 'La descripción es obligatoria.'
        if not precio:
            errores['precio'] = 'El precio es obligatorio.'
        else:
            try:
                precio_float = float(precio)
                if precio_float < 0:
                    errores['precio'] = 'El precio no puede ser menor a 0.'
            except Exception:
                errores['precio'] = 'El precio debe ser un número.'
        if not categoria_id:
            errores['categoria_id'] = 'Debe seleccionar una categoría.'

        if not errores:
            ProductoService.crear({
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'categoria_id': categoria_id
            })
            return redirect(url_for('producto.listar'))
        else:
            return render_template('productos/form.html', categorias=categorias, accion='Crear', errores=errores)
    return render_template('productos/form.html', categorias=categorias, accion='Crear')

@producto_bp.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    producto = ProductoService.obtener(id)
    categorias = ProductoService.categorias()
    errores = {}
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        precio = request.form.get('precio', '').strip()
        categoria_id = request.form.get('categoria_id', '').strip()

        # Validaciones
        if not nombre:
            errores['nombre'] = 'El nombre es obligatorio.'
        if not descripcion:
            errores['descripcion'] = 'La descripción es obligatoria.'
        if not precio:
            errores['precio'] = 'El precio es obligatorio.'
        else:
            try:
                precio_float = float(precio)
                if precio_float < 0:
                    errores['precio'] = 'El precio no puede ser menor a 0.'
            except Exception:
                errores['precio'] = 'El precio debe ser un número.'
        if not categoria_id:
            errores['categoria_id'] = 'Debe seleccionar una categoría.'

        if not errores:
            ProductoService.actualizar({
                'id': id,
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'categoria_id': categoria_id
            })
            return redirect(url_for('producto.listar'))
        else:
            # Se muestra el formulario con errores e info actualizada
            producto_data = {
                'id': id,
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'categoria_id': int(categoria_id) if categoria_id else None
            }
            return render_template('productos/form.html', producto=producto_data, categorias=categorias, accion='Editar', errores=errores)
    return render_template('productos/form.html', producto=producto, categorias=categorias, accion='Editar')

@producto_bp.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoService.eliminar(id)
    return redirect(url_for('producto.listar'))
