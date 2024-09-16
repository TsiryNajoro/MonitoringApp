import csv
from datetime import datetime
import os

def parse_log_line(log_line):
    try:
        # Extraire la date et l'heure du début de la ligne
        date_str, rest_of_line = log_line.split(',', 1)
        # Convertir la chaîne de date en objet datetime
        event_time = datetime.strptime(date_str, '%Y%m%d %H:%M:%S')
        return event_time, rest_of_line
    except ValueError as e:
        print(f"Erreur de format pour la ligne: {log_line.strip()}")
        print(f"Exception: {e}")
        return None, None

def process_log_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return

    with open(file_path, 'r') as file:
        for line in file:
            # Supposer que chaque ligne est un enregistrement CSV
            event_time, rest_of_line = parse_log_line(line)
            if event_time:
                # Traiter les données restantes de la ligne si la date est correctement parsée
                data = rest_of_line.split(',')
                # Faites ce que vous devez faire avec les données ici
                print(f"Date et Heure: {event_time}, Données: {data}")

def main():
    log_file_path = "C:/wamp64/logs/server_audit.log"  # Chemin vers votre fichier log
    process_log_file(log_file_path)

if __name__ == "__main__":
    main()
