from flask import Blueprint, jsonify
from .models import AuditLog

# Crée un blueprint pour l'application
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Audit Log Monitoring App is running"

@main.route('/audit_logs', methods=['GET'])
def get_audit_logs():
    # Récupère tous les logs d'audit depuis la base de données
    logs = AuditLog.query.all()
    result = [
        {
            'id': log.id,
            'server_id': log.server_id,
            'event_time': log.event_time,
            'user_host': log.user_host,
            'query': log.query,
            'database': log.database,
            'table_name': log.table_name,
            'operation': log.operation
        }
        for log in logs
    ]
    return jsonify(result)
