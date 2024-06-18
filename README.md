# StyleHome

## Descripción
Este es el proyecto Django para "StyleHome". Es una aplicación web diseñada para la venta de muebles y otros bienes de hogar.

## Configuración Inicial

Para ejecutar este proyecto localmente, sigue los siguientes pasos:

### Prerrequisitos
- Python 3.x
- pip
- virtualenv (opcional)

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/AlexOT03/StyleHome
```


2. Navega al directorio del proyecto:

```bash
cd StyleHome
```


3. (Opcional) Crea y activa un entorno virtual:

```bash
virtualenv venv source venv/bin/activate 
# En Windows usa: venv\Scripts\activate
```


4. Instala las dependencias:

```bash
pip install -r requirements.txt
```


5. Copia el archivo `.env.example` a `.env` y ajusta las variables de entorno según sea necesario.

6. Realiza las migraciones necesarias:

```bash
python manage.py migrate
```


7. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```
Ahora deberías poder acceder al servidor de desarrollo en [http://localhost:8000](http://localhost:8000).

## Creacion de apps

1. Crea un nuevo directorio dentro de la carpeta `apps` con el nombre de la aplicación.

```bash
stylehome
└───apps
    └───new_app_folder
```

2. Ejecutar en la terminal el comando _(recuerda que el folder y la app deben tener el mismo nombre)_:

```bash
pythin manage.py startapp nombre_app stylehome/apps/nombre_app
```

3. En el archivo `apps.py` de la app creada, configura el nombre de la aplicación.

```python
class Name_AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stylehome.apps.name_app'
```

4. Agrega el path de tu app en el archivo `settings.py`. Por ejemplo, si creaste una app llamada "mi_app", debes agregar la línea `LOCAL_APPS = ['stylehome.apps.mi_app']`.

Ejemplo:
```python
LOCAL_APPS = [
    # ...
    'stylehome.apps.mi_app',
]
```

## Licencia

Este proyecto está bajo la Licencia (en progreso). Consulta el archivo LICENSE.md para más detalles.

## Autores

- [@AlexOT03](https://github.com/AlexOT03)