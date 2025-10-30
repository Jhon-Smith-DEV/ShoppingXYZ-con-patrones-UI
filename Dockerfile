# Usa una imagen ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /code

# Variables de entorno para que Python y Flask funcionen correctamente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Instala dependencias del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto 5000 (para Flask) ← opcional, pero buena práctica
EXPOSE 5000

# Comando de inicio: ejecutar Flask directamente
CMD ["flask", "run"]
