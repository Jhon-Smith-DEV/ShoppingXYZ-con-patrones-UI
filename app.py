from flask import Flask, render_template
from presentation.routes_categoria import categoria_bp
from presentation.routes_producto import producto_bp
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(producto_bp, url_prefix="/productos")
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('base.html')

# if __name__ == '__main__':
#     os.environ.setdefault('FLASK_APP', 'app.py')
#     # app.run(host='0.0.0.0', port=5000, debug=True)
#     app.run(host='127.0.0.1', port=5001, debug=True)
