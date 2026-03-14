# KPI Manager API

API REST desarrollada en Python para la gestión de indicadores de desempeño (KPIs) empresariales.

Este proyecto fue desarrollado como práctica de arquitectura backend utilizando tecnologías modernas del ecosistema Python.

## 🚀 Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Passlib (hash de contraseñas)
- Uvicorn

## 📊 Funcionalidades

### Autenticación

- Registro de usuarios
- Login con JWT
- Protección de endpoints mediante token

### Gestión de KPIs

- Crear KPI
- Listar KPIs
- Consultar KPI por ID
- Actualizar KPI
- Eliminar KPI

## 🔐 Seguridad

- Contraseñas almacenadas con hash bcrypt
- Autenticación mediante JSON Web Tokens
- Endpoints protegidos

## 📂 Estructura del proyecto

app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── dependencies.py
├── security.py
└── routers/


## ⚙️ Instalación

- Clonar repositorio:

git clone https://github.com/tuusuario/kpi-manager-api.git
cd kpi-manager-api


python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

## 📖 Documentación API

- La documentación automática está disponible en:

http://localhost:8000/docs


## 🎯 Objetivo del proyecto

- Este proyecto demuestra la construcción de una API backend completa utilizando Python, aplicando buenas prácticas de arquitectura, autenticación y manejo de base de datos.


