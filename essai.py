from sqlalchemy import create_engine

# Utiliser mariadb+mysqldb pour MariaDB
DATABASE_URL = 'mariadb+mariadbconnector://root:jojo@localhost/audit_db'
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Connexion réussie à MariaDB!")
except Exception as e:
    print(f"Erreur de connexion: {e}")
