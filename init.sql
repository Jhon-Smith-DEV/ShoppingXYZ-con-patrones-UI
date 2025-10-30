-- init.sql: create tables for categorias and productos

DROP TABLE IF EXISTS productos CASCADE;
DROP TABLE IF EXISTS categorias CASCADE;

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    categoria_id INTEGER NOT NULL,
    CONSTRAINT fk_categoria
        FOREIGN KEY (categoria_id)
        REFERENCES categorias (id)
        ON DELETE CASCADE
);

-- =========================================
-- Script de inserción de datos iniciales
-- Proyecto: GraphQL Supermercado
-- Tablas: categorias, productos
-- =========================================

-- Limpieza de tablas (opcional)
TRUNCATE TABLE productos RESTART IDENTITY CASCADE;
TRUNCATE TABLE categorias RESTART IDENTITY CASCADE;

-- =========================================
-- Categorías
-- =========================================
INSERT INTO categorias (nombre, descripcion) VALUES
('Frutas y Verduras', 'Productos frescos del campo, frutas y hortalizas.'),
('Lácteos', 'Leche, yogures, quesos y otros derivados.'),
('Bebidas', 'Jugos, gaseosas, aguas y bebidas energéticas.'),
('Abarrotes', 'Productos no perecederos y de despensa básica.');

-- =========================================
-- Productos
-- =========================================
INSERT INTO productos (nombre, descripcion, precio, categoria_id) VALUES
-- Frutas y Verduras (id = 1)
('Manzana Roja', 'Manzana fresca de temporada', 0.80, 1),
('Banano', 'Banano ecuatoriano dulce y maduro', 0.50, 1),
('Tomate Riñón', 'Tomate fresco ideal para ensaladas', 1.20, 1),
('Zanahoria', 'Zanahoria orgánica por libra', 0.90, 1),
('Lechuga Romana', 'Lechuga fresca y crujiente', 1.00, 1),

-- Lácteos (id = 2)
('Leche Entera 1L', 'Leche entera pasteurizada', 1.25, 2),
('Queso Mozzarella 250g', 'Queso mozzarella rallado', 3.50, 2),
('Yogur Natural 1L', 'Yogur natural sin azúcar', 2.10, 2),
('Mantequilla 200g', 'Mantequilla de vaca sin sal', 2.40, 2),
('Crema de Leche 200ml', 'Crema de leche pasteurizada', 1.80, 2),

-- Bebidas (id = 3)
('Agua Mineral 500ml', 'Agua mineral sin gas', 0.75, 3),
('Jugo de Naranja 1L', 'Jugo natural de naranja', 2.50, 3),
('Coca-Cola 2L', 'Bebida gaseosa sabor cola', 2.90, 3),
('Cerveza Rubia 330ml', 'Cerveza artesanal tipo lager', 1.80, 3),
('Bebida Energética 250ml', 'Energizante sabor tropical', 2.20, 3),

-- Abarrotes (id = 4)
('Arroz Blanco 1kg', 'Arroz grano largo de primera calidad', 1.60, 4),
('Aceite Vegetal 1L', 'Aceite de girasol refinado', 3.40, 4),
('Azúcar 1kg', 'Azúcar blanca refinada', 1.50, 4),
('Sal 1kg', 'Sal de mesa yodada', 0.90, 4),
('Harina de Trigo 1kg', 'Harina blanca de trigo fortificada', 2.10, 4);

-- =========================================
-- Fin del script
-- =========================================
