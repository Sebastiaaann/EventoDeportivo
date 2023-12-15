# EventoDeportivo


-- Primero Crear entorno VENV
#   VENV
python -m venv nombre_del_entorno

nombre_del_entorno\Scripts\Activate

pip install -r requirements.txt

# PIP Necesarios para que funcione

pip install django

pip install django-widget-tweaks

# PDF
pip install reportlab

# EXCEL
pip install openpyxl




-- Migraciones
# Hacer migraciones

python manage.py migrate
python manage.py makemigrations

