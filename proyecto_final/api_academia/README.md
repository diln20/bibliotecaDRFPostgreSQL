# API Academia - proyecto final

Proyecto de apoyo para la biblioteca DRF + PostgreSQL Academy.

## 1. Crear base y usuario

```sql
CREATE ROLE api_academia_user WITH LOGIN PASSWORD 'cambia_esta_clave';
CREATE DATABASE api_academia_db OWNER api_academia_user;
```

## 2. Crear entorno e instalar

```bash
python -m venv .venv
pip install -r requirements.txt
```

## 3. Variables

Copia `.env.example` a `.env` y ajusta la contraseña.

## 4. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rutas

- `GET/POST /api/programas/`
- `GET/PATCH/DELETE /api/programas/{id}/`
- `GET/POST /api/estudiantes/`
- `GET/PATCH/DELETE /api/estudiantes/{id}/`
- `POST /api-token-auth/`
- `GET /admin/`

Filtros de estudiantes:

- `?activo=true`
- `?programa=1`
- `?nombre=ana`
