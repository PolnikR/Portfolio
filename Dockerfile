# Použijeme oficiálny Python obraz
FROM python:3.12

# Nastavenie pracovného adresára v kontajneri
WORKDIR /app

# Kopírovanie požiadaviek do kontajnera
COPY requirements.txt /app/

# Inštalácia závislostí
RUN pip install --no-cache-dir -r requirements.txt

# Kopírovanie celého projektu do kontajnera
COPY . /app/

# Spustenie migrácií a zbieranie statických súborov
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expozícia portu
EXPOSE 8000

# Definícia príkazu na spustenie aplikácie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]