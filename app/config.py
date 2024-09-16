import os

class Config:
    # Utilise les variables d'environnement pour stocker les informations sensibles
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mariadb+mariadbconnector://root:jojo@localhost/audit_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
