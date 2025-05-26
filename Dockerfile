# Utilise une image de base Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exposer le port de Flask
EXPOSE 5000

# Commande pour lancer l’application Flask
CMD ["python", "app.py"]
