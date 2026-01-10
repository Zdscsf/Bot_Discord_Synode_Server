# Dockerfile
FROM python:3.11-slim

# Dossier de travail dans le container
WORKDIR /app

# Copier tous les fichiers du dépôt dans le container
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip && pip install fastapi uvicorn httpx

# Exposer le port 8000 pour l'API
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "Place_FastAPI:app", "--host", "0.0.0.0", "--port", "8000"]

